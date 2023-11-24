from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .pagination import ProductResultsSetPagination

from product.models import Product
from .serializers import ProductViewOutputSerializer
from rest_framework.decorators import action

class ProductViewSet(ReadOnlyModelViewSet):
    
    queryset = Product.objects.all()
    serializer_class = ProductViewOutputSerializer

    pagination_class = ProductResultsSetPagination
    filter_backends = [
        DjangoFilterBackend
    ]

    # filterset_fields = [
    #     'price_amount'
    # ]

    