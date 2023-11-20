
# DRF imports
from rest_framework import serializers

from product.models import (
    ProductTag,
)



class ProductTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTag
        fields = ("id", "name", )
