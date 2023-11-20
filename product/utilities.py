
import json
from apiclient.exceptions import APIClientError

from product.api_client import ProductAPIClient
from product.models import Product
from product.api.serializers import ProductSerializer


class ProductUtility: 
    ...
    @classmethod
    def populate_database(self, merchant_id, access_token):
        client = ProductAPIClient.client(access_token)

        all_products_pages = client.get_all_products()
        Product.objects.filter(merchant_id=merchant_id).delete()
        for products_page in all_products_pages: 
            # [{...}, ..., {...}]
            for product in products_page:
                product["merchant"] = merchant_id
                serializer = ProductSerializer(data=product)
                if serializer.is_valid():
                    instance = serializer.save()
                    # create related models
                    ProductUtility.create_product_price(instance, product["price"])
                else:
                    raise APIClientError(json.dumps(serializer.errors))
    
    @classmethod
    def get_product_by_id(self, product_id):
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return None

    @classmethod
    def create_product(self, merchant_id, product_data):
       
        product_data["merchant"] = merchant_id
        serializer = ProductSerializer(data=product_data)
        if not serializer.is_valid():
            raise APIClientError(json.dumps(serializer.errors))
        product = serializer.save()

        # create related models
        ProductUtility.create_product_price(product, product_data["price"])

    @classmethod
    def update_product(self, merchant_id, product_data):
        product = self.get_product_by_id(product_data["id"])
        if not product:
            self.create_product(merchant_id, product_data)
            return product
        product_data["merchant"] = merchant_id
        serializer = ProductSerializer(product, data=product_data)
        if not serializer.is_valid():
            raise APIClientError(json.dumps(serializer.errors))
        
        return serializer.save()

    @classmethod
    def delete_product(self, merchant_id, product_id):
        product = self.get_product_by_id(product_id)
        if product:
            v = product.delete()
        return True

    # @classmethod
    # def create_product_price(self, product_id, price_dict):
    #     ProductPrice.objects.create(
    #         product=product_id,
    #         **price_dict
    #         )
    #     return True




