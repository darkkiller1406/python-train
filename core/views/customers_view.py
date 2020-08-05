from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from core.models import Customers
from core.views.filters import CustomersFilter
from core.views.serializers import CustomersSerializer


class CustomersView(ListAPIView):
    pagination_class = None
    queryset = Customers.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomersSerializer
    filter_class = CustomersFilter
