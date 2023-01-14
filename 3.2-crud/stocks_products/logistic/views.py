from rest_framework.viewsets import ModelViewSet
#from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации
    #DEFAULT_FILTER_BACKENDS в setting.py
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']
    
class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    #при необходимости добавьте параметры фильтрации
    filterset_fields = ['products',]

    pagination_class = LimitOffsetPagination