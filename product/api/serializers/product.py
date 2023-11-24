from rest_framework import serializers

from product.models import Product
from .product_tag import ProductTagSerializer


class ProductViewOutputSerializer(serializers.ModelSerializer):
    tags = ProductTagSerializer(read_only=True, many=True)
 
    class Meta:
        model = Product
        fields = (
            "id", "name", "description",
            # prices
            "price", "sale_price", "cost_price",
            "tags",
        )

    def get_rating(self, instance):
        total = instance.get_rating_total()
        count = instance.get_rating_count()
        avg_rating = instance.get_rating_avg()

        data = {
            "total": total,
            "count": count,
            "rate": avg_rating,
        }

        return data

