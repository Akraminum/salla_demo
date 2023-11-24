from hook.event_handlers.base import BaseEventHandler
from category.utilities import CategoryUtility
from category.api_client.serializers import CategorySeedSerializer

from django.db import connection

class CategoryEventHandler(BaseEventHandler):
    name = "ProductEventHandler"
    serializer = CategorySeedSerializer

    def clean_data(self, merchant_id, event):
        event["merchant_id"] = merchant_id
        # deserialize event data 
        ser = self.serializer(data=event)
        ser.is_valid(raise_exception=True)
        return ser.validated_data

    def created(self, merchant_id, event):
        print('******** created category *********')

        mapped_data = self.clean_data(merchant_id, event)
        # [print(q) for q in connection.queries]

        category = CategoryUtility.create_category(mapped_data)
        
        if not category:
            return False
        # event custom logic
        ...
        return True
    
    def updated(self, merchant_id, event):
        print('******** updated category *********')
        mapped_data = self.clean_data(merchant_id, event)
        # [print(q) for q in connection.queries]
        category = CategoryUtility.update_category(merchant_id, event)
        return True if category else False
    
    def deleted(self, merchant, event):
        ...
        print('******** deleted category *********')
        return CategoryUtility.delete_category(event["id"])
