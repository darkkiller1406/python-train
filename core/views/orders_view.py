from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from core.models import Orders, OrderItems
from core.views.filters import OrdersFilter, OrderItemsFilter
from core.views.serializers import OrdersSerializer


class OrdersView(ListAPIView):
    pagination_class = None
    queryset = Orders.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = OrdersSerializer
    filter_class = OrdersFilter


class OrderItemsView(ListAPIView):
    pagination_class = None
    queryset = OrderItems.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = OrdersSerializer
    filter_class = OrderItemsFilter
