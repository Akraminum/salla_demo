from rest_framework import serializers

from product.models import Product
from .product_tag import ProductTagSerializer


class ProductSerializer(serializers.ModelSerializer):
    tags = ProductTagSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "merchant",
            "name",
            "description",
            "price",
            "regular_price",
            "tags",
            "images",
        )

    def get_links(self, instance):
        request = self.context["request"]

    #     add_comment = reverse("api:products-add-comment", args=[instance.id])
    #     add_to_favorite = reverse("api:products-add-to-favorite", args=[instance.id])
    #     remove_from_favorite = reverse("api:products-remove-from-favorite", args=[instance.id])
    #     add_to_cart = reverse("api:products-add-to-cart", args=[instance.id])
    #     remove_from_cart = reverse("api:products-remove-from-cart", args=[instance.id])
    #     delete_from_cart = reverse("api:products-delete-from-cart", args=[instance.id])

    #     data = {
    #         "detail": request.build_absolute_uri(detail),
    #         "add_comment": request.build_absolute_uri(add_comment),
    #         "add_to_favorite": request.build_absolute_uri(add_to_favorite),
    #         "remove_from_favorite": request.build_absolute_uri(remove_from_favorite),
    #         "add_to_cart": request.build_absolute_uri(add_to_cart),
    #         "remove_from_cart": request.build_absolute_uri(remove_from_cart),
    #         "delete_from_cart": request.build_absolute_uri(delete_from_cart),
    #     }

    #     return data
        return {}

    def get_quantity(self, instance):
        return instance.get_product_quantity()

    def get_sold_quantity(self, instance):
        return instance.get_product_sold_quantity()

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

