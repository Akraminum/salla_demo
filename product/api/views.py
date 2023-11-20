from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from .pagination import ProductResultsSetPagination
from django_filters.rest_framework import DjangoFilterBackend




from product.models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import action

class ProductViewSet(ReadOnlyModelViewSet):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

    pagination_class = ProductResultsSetPagination
    filter_backends = [
        DjangoFilterBackend
    ]
    filterset_fields = [
        'price__amount'
    ]

    