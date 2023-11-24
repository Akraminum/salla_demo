
import json
from apiclient.exceptions import APIClientError

from product.api_client import ProductAPIClient
from product.models import Product
from product.models.crazy import ProductTag
from .serializers import ProductSeedSerializer, ProductTagSeedSerializer

from django.db import connection

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
                serializer = ProductSeedSerializer(data=product)
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
        serializer = ProductSeedSerializer(data=product_data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        # create related models
        if product_data.get("tags", []).__len__ > 0:
            ProductUtility.update_product_tags(instance, product_data.get("tags"))
        return instance

    @classmethod
    def update_product(self, merchant_id, product_data):
        product = self.get_product_by_id(product_data["id"])
        if not product:
            instance = self.create_product(merchant_id, product_data)
        
        product_data["merchant"] = merchant_id
        serializer = ProductSeedSerializer(product, data=product_data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        # create related models
        if product_data.get("tags", []).__len__() > 0:
            ProductUtility.update_product_tags(instance, product_data.get("tags"))
        return instance
        

    @classmethod
    def delete_product(self, merchant_id, product_id):
        product = self.get_product_by_id(product_id)
        if product:
            v = product.delete()
        return True

    @classmethod
    def update_product_tags(self, product: Product, tags_list: [{}]):
        ...
        # for each tag in tags_list
        # get or create tage 
        # tag = {id: 1, name: "tag1"}
        new_tags = []
        for tag in tags_list:
            if not (ProductTag.objects.filter(id=tag["id"]).exists()):
                new_tags.append(tag)
                
        # create new tags in bulck
        if new_tags.__len__() > 0:
            serializer = ProductTagSeedSerializer(data=new_tags, many=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            
        # set tag_list ids to product
        tags_list_ids = [tag["id"] for tag in tags_list]
        product.tags.set(tags_list_ids)      




