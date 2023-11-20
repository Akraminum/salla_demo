# Django imports
from django.urls import reverse

# DRF imports
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

# Local imports
from .models import (
    Product,
    ProductImage,
    ProductOption,
    ProductOptionValue,
    ProductOptionValuePrice,
    ProductPrice,
    ProductRegularPrice,
    ProductTag,
)




class ProductPriceSerializer(serializers.ModelSerializer):
    """
    Serialize the `price` of a product.
    """

    class Meta:
        model = ProductPrice
        fields = ("amount", "currency")

    # def create(self, validated_data):
    #     raise RuntimeError("You cannot create a product from the API.")

    # def update(self, instance, validated_data):
    #     raise RuntimeError("You cannot update a product from the API.")


class ProductRegularPriceSerializer(serializers.ModelSerializer):
    """
    Serialize the `regular_price` of a product.
    """

    class Meta:
        model = ProductRegularPrice
        fields = ("amount", "currency")

    # def create(self, validated_data):
    #     raise RuntimeError("You cannot create a product from the API.")

    # def update(self, instance, validated_data):
    #     raise RuntimeError("You cannot update a product from the API.")


class ProductOptionValuePriceSerializer(serializers.ModelSerializer):
    """
    Serialize the `price` of a product option value.
    """

    class Meta:
        model = ProductOptionValuePrice
        fields = ("amount", "currency")

    # def create(self, validated_data):
    #     raise RuntimeError("You cannot create a product from the API.")

    # def update(self, instance, validated_data):
    #     raise RuntimeError("You cannot update a product from the API.")


class ProductOptionValueSerializer(serializers.ModelSerializer):
    """
    Serialize the `values` of a product option.
    """

    price = ProductOptionValuePriceSerializer(read_only=True)

    class Meta:
        model = ProductOptionValue
        fields = (
            "id",
            "name",
            "display_value",
            "image_url",
            "is_default",
            "price",
        )

    # def create(self, validated_data):
    #     raise RuntimeError("You cannot create a product from the API.")

    # def update(self, instance, validated_data):
    #     raise RuntimeError("You cannot update a product from the API.")


class ProductOptionSerializer(serializers.ModelSerializer):
    """
    Serialize the `options` of a product.
    """

    values = ProductOptionValueSerializer(read_only=True, many=True)

    class Meta:
        model = ProductOption
        fields = (
            "id",
            "name",
            "description",
            "type",
            "required",
            "sort",
            "display_type",
            "visibility",
            "visibility_condition_type",
            "visibility_condition_option",
            "visibility_condition_value",
            "values",
        )

    # def create(self, validated_data):
    #     raise RuntimeError("You cannot create a product from the API.")

    # def update(self, instance, validated_data):
    #     raise RuntimeError("You cannot update a product from the API.")


class ProductTagSerializer(serializers.ModelSerializer):
    """
    Serialize the `tags` of a product.
    """

    class Meta:
        model = ProductTag
        fields = (
            "id",
            "name",
        )

    # def create(self, validated_data):
    #     raise RuntimeError("You cannot create a product from the API.")

    # def update(self, instance, validated_data):
    #     raise RuntimeError("You cannot update a product from the API.")


class ProductImageSerializer(serializers.ModelSerializer):
    """
    Serialize the `images` of a product.
    """

    class Meta:
        model = ProductImage
        fields = (
            "id",
            "url",
            "main",
            "three_d_image_url",
            "alt",
            "video_url",
            "type",
            "sort",
        )

    # def create(self, validated_data):
    #     raise RuntimeError("You cannot create a product from the API.")

    # def update(self, instance, validated_data):
    #     raise RuntimeError("You cannot update a product from the API.")


class ProductLinkSerializer(serializers.Serializer):
    detail = serializers.URLField()
    add_comment = serializers.URLField()
    add_to_favorite = serializers.URLField()
    remove_from_favorite = serializers.URLField()
    add_to_cart = serializers.URLField()
    remove_from_cart = serializers.URLField()
    delete_from_cart = serializers.URLField()

    # update detail validations
    def validate_detail(self, value):
        if value.startswith("http://testserver"):
            return value
        else:
            return super().validate_detail(value)


class ProductRatingSerializer(serializers.Serializer):
    total = serializers.IntegerField()
    count = serializers.IntegerField()
    rate = serializers.FloatField()


# class PriceSerializer(serializers.Serializer):
#     ...
#     amount = serializers.DecimalField()
#     currency = serializers.CharField()



# PRODUCT SERIALIZER
class ProductSerializer(serializers.ModelSerializer):
    """
    Serialize a product.
    """
    
    # links = serializers.SerializerMethodField()
    # rating = serializers.SerializerMethodField()
    price = ProductPriceSerializer(read_only=True)
    regular_price = ProductRegularPriceSerializer(read_only=True)
    # quantity = serializers.SerializerMethodField()
    # sold_quantity = serializers.SerializerMethodField()
    options = ProductOptionSerializer(read_only=True, many=True)
    tags = ProductTagSerializer(read_only=True, many=True)
    # comments = ProductCommentSerializer(read_only=True, many=True)
    images = ProductImageSerializer(read_only=True, many=True)
    # categories = ProductCategorySerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = (
            "merchant",
            "id",
            # "links",
            "name",
            "description",
            # "rating",
            "price",
            "regular_price",
            # "quantity",
            # "sold_quantity",
            "options",
            # "categories",
            "tags",
            # "comments",
            "images",
        )


    # def create(self, validated_data):
    #     raise RuntimeError("You cannot create a product from the API.")

    # def update(self, instance, validated_data):
    #     raise RuntimeError("You cannot update a product from the API.")

    def get_links(self, instance):
        request = self.context["request"]

    #     detail = reverse("api:products-detail", args=[instance.id])
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

