from rest_framework import serializers
from product.models import Product


from product.models import (
    ProductTag,
)
class ProductTagSeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTag
        fields = ("id", "name", )


# api response to internal model
class ProductSeedSerializer(serializers.ModelSerializer):
    # tags = ProductTagSeedSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            "id", "name", "description",
            # "price",
            "price_amount", "taxed_price_amount",
            "pre_tax_price_amount", "tax_amount",
            # "cost_price", 
            "regular_price_amount",
            "price_currency",
            "merchant", 
            # "tags",
        )
    
    def to_internal_value(self, data):
        data["price_amount"] = data["price"]["amount"]
        data["price_currency"] = data["price"]["currency"]
        data["taxed_price_amount"] = data["taxed_price"]["amount"]
        data["pre_tax_price_amount"] = data["pre_tax_price"]["amount"]
        data["tax_amount"] = data["tax"]["amount"]
        data["regular_price_amount"] = data["regular_price"]["amount"]
        return super().to_internal_value(data)

    def create(self, validated_data):
        return super().create(validated_data)

    


r = {
    "id": 1962371407,
    "promotion": {
      "title": '"null"',
      "sub_title": '"null"'
    },
    "sku": "",
    "mpn": 'null',
    "gtin": 'null',
    "type": "product",
    "name": "porduct pordy purparosta",
    "short_link_code": "ydwxQZZ",
    "urls": {
      "customer": "https://salla.sa/dev-jhnmyomat2m1nqve/jghhgggh/p1962571407",
      "admin": "https://s.salla.sa/products/1962571407"
    },
    "price": {
      "amount": 567,
      "currency": "SAR"
    },
    "taxed_price": {
      "amount": 567,
      "currency": "SAR"
    },
    "pre_tax_price": {
      "amount": 567,
      "currency": "SAR"
    },
    "tax": {
      "amount": 0,
      "currency": "SAR"
    },
    "description": "",
    "quantity": 'null',
    "status": "hidden",
    "is_available": 'false',
    "views": 0,
    "sale_price": {
      "amount": 0,
      "currency": "SAR"
    },
    "sale_end": 'null',
    "require_shipping": 'true',
    "cost_price": "",
    "weight": 0,
    "weight_type": "kg",
    "with_tax": 'true',
    "url": "https://salla.sa/dev-jhnmyomat2m1nqve/jghhgggh/p1962571407",
    "main_image": "",
    "images": [],
    "sold_quantity": 0,
    "rating": {
      "total": 0,
      "count": 0,
      "rate": 0
    },
    "regular_price": {
      "amount": 567,
      "currency": "SAR"
    },
    "max_items_per_user": 0,
    "maximum_quantity_per_order": 'null',
    "show_in_app": 'false',
    "notify_quantity": 0,
    "hide_quantity": "false",
    "unlimited_quantity": "false",
    "managed_by_branches": "false",
    "services_blocks": {
      "installments": []
    },
    "calories": 'null',
    "customized_sku_quantity": "false",
    "channels": [],
    "metadata": {
      "title": 'null',
      "description": 'null',
      "url": 'null'
    },
    "allow_attachments": "false",
    "is_pinned": "false",
    "pinned_date": "2023-11-18 14:39:30",
    "sort": 0,
    "enable_upload_image": "false",
    "updated_at": "2023-11-18 14:39:30",
    "options": [],
    "skus": [],
    "categories": [
      {
        "id": 22668724,
        "name": "البلايز",
        "urls": {
          "customer": "https://salla.sa/dev-jhnmyomat2m1nqve/البلايز/c22668724",
          "admin": "https://s.salla.sa/categories"
        },
        "items": [],
        "parent_id": 0,
        "status": "active",
        "sort_order": 11,
        "update_at": "2023-11-18 14:20:20",
        "metadata": {
          "title": "null",
          "description": "null",
          "url": "null"
        },
        "sub_categories": []
      }
    ],
    "brand": "null",
    "tags": []
  }