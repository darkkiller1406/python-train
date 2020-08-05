from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Max


class VarCharField(models.CharField):
    """
    A basically unlimited-length CharField.
    """
    description = "Unlimited-length string"

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = int(1e9)
        super(models.CharField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return 'VarCharField'

    def db_type(self, connection):
        return 'varchar'

    def formfield(self, **kwargs):
        return super(models.CharField, self).formfield(**kwargs)


class Customers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=10000)
    phone = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return '{} {}'.format(self.last_name, self.first_name)


class Orders(models.Model):
    barcode = models.CharField(unique=True, max_length=10)
    customers = models.ForeignKey('Customers', on_delete=models.CASCADE)
    status = models.CharField(max_length=50)  # must custom to select option
    employee = models.ForeignKey('Employees', on_delete=models.CASCADE)
    order_date = models.DateField()

    def save(self, *arg, **kwargs):
        if not self.barcode:
            max_id = Orders.objects.aggregate(barcode_max=Max('id'))['barcode_max']
            self.barcode = "{}{:05d}".format('A', max_id if max_id is not None else 1)
        super().save(*arg, **kwargs)


class Employees(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    hire_date = models.DateField()
    job_title = VarCharField(null=True, blank=True)


class OrderItems(models.Model):
    order = models.ForeignKey('Orders', on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    unite_price = models.IntegerField()
    product = models.ForeignKey('Products', on_delete=models.CASCADE)


class Products(models.Model):
    product_name = models.CharField(max_length=10000)
    barcode = models.CharField(unique=True, max_length=10)
    description = VarCharField(null=True, blank=True)
    standard_cost = models.IntegerField()
    list_price = models.IntegerField()
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    category = models.ForeignKey('ProductCategories', on_delete=models.DO_NOTHING, blank=True, null=True)
    image_url = VarCharField(null=True, blank=True)

    def save(self, *arg, **kwargs):
        if not self.barcode:
            max_id = Products.objects.aggregate(barcode_max=Max('id'))['barcode_max']
            self.barcode = "{}{:05d}".format('A', max_id if max_id is not None else 1)
        super().save(*arg, **kwargs)

    def __str__(self):
        return self.product_name


class ProductCategories(models.Model):
    category_name = models.CharField(max_length=10000)

    def __str__(self):
        return self.category_name




