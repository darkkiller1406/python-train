from rest_framework.serializers import ModelSerializer

from core.models import Products, Customers, Orders, ProductCategories


class ProductsSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class ProductCategoriesSerializer(ModelSerializer):
    class Meta:
        model = ProductCategories
        fields = '__all__'


class CustomersSerializer(ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'


class OrdersSerializer(ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'
