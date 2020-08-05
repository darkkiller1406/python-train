from django_filters import rest_framework as filters

from core.models import Products, Customers, Orders, OrderItems


class ProductsFilter(filters.FilterSet):
    product_name = filters.CharFilter(method='filter_product_name')

    @staticmethod
    def filter_product_name(queryset, name, value):
        return queryset.filter(product_name__icontains=value)

    class Meta:
        model = Products
        fields = ['product_name']


class ProductCategoriesFilter(filters.FilterSet):
    category_name = filters.CharFilter(method='filter_product_category_name')

    @staticmethod
    def filter_product_category_name(queryset, name, value):
        return queryset.filter(category_name__icontains=value)

    class Meta:
        model = Products
        fields = ['category_name']


class CustomersFilter(filters.FilterSet):
    phone = filters.CharFilter(method='filter_customer_phone')

    @staticmethod
    def filter_customer_phone(queryset, name, value):
        return queryset.filter(phone__iexact=value)

    class Meta:
        model = Customers
        fields = ['phone']


class OrdersFilter(filters.FilterSet):
    barcode = filters.CharFilter(method='filter_order_barcode')

    @staticmethod
    def filter_order_barcode(queryset, name, value):
        return queryset.filter(barcode__iexact=value)

    class Meta:
        model = Orders
        fields = ['barcode']


class OrderItemsFilter(filters.FilterSet):
    order_barcode = filters.CharFilter(method='filter_barcode_order')
    product_barcode = filters.CharFilter(method='filter_product_barcode')

    @staticmethod
    def filter_barcode_order(queryset, name, value):
        return queryset.filter(order__barcode__iexact=value)

    @staticmethod
    def filter_product_barcode(queryset, name, value):
        return queryset.filter(product__barcode__iexact=value)

    class Meta:
        model = OrderItems
        fields = ['order', 'product']
