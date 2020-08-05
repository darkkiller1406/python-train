from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from core.models import Products, ProductCategories
from core.views.filters import ProductsFilter, ProductCategoriesFilter
from core.views.serializers import ProductsSerializer


class ProductsView(ListAPIView):
    pagination_class = None
    queryset = Products.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductsSerializer
    filter_class = ProductsFilter


class ProductCategoriesView(ListAPIView):
    pagination_class = None
    queryset = ProductCategories.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductsSerializer
    filter_class = ProductCategoriesFilter
