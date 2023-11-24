
import json
from .models import Category
from .api_client.serializers import CategorySeedSerializer
from .api_client import CategoryAPIClient


class CategoryUtility:
    ...
    @classmethod
    def populate_database(self, merchant_id, access_token):
        client:CategoryAPIClient = CategoryAPIClient.client(access_token)

        all_pages = client.get_all_categories()
        Category.objects.filter(merchant_id=merchant_id).delete()
        for page in all_pages: 
            # [{...}, ..., {...}]
            for category_data in page:
                category_data['merchant_id'] = merchant_id
                CategoryUtility.create_category(category_data)
        return True

    @classmethod
    def create_category(self, category_data):
        subs = category_data.pop('items', None)
        instance = Category.objects.create(**category_data)

        # check for childs list
        if subs:
            for sub_category in subs:
                sub_category['merchant_id'] = category_data['merchant_id']
                sub_category["parent_id"] = category_data["id"]
                CategoryUtility.create_category(sub_category)
        
        return instance 

    @classmethod
    def get_category_by_id(self, category_id):
        try:
            category = Category.objects.get(id=category_id)
            return category
        except Category.DoesNotExist:
            return None
    
    @classmethod
    def update_category(self, merchant_id, category_data):
        category_data["merchant_id"] = merchant_id
        category = CategoryUtility.get_category_by_id(category_data["id"])
        if not category:
            CategoryUtility.create_category( category_data)
            return category
        
        category_data["merchant"] = merchant_id
        serializer = CategorySeedSerializer(category, data=category_data)
        
        serializer.is_valid(raise_exception=True)
        return serializer.save()

    @classmethod
    def delete_category(self, category_id):
        category = CategoryUtility.get_category_by_id(category_id)
        if category:
            category.delete()
            return True
        return False



