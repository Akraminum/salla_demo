from hook.event_handlers.base import BaseEventHandler
from .utilities import ProductUtility

class ProductEventHandler(BaseEventHandler):
    name = "ProductEventHandler"

    def created(self, merchant_id, event):
        print('******** created product *********')
        product = ProductUtility.create_product(merchant_id, event)
        if not product:
            return False
        # event custom logic
        ...
        return True
        
    def updated(self, merchant, event):
        print('******** updated product *********')
        product = ProductUtility.update_product(merchant, event)
        if not product:
            return False
        return True
    
    def deleted(self, merchant, event):
        ...
        print('******** deleted product *********')
        return ProductUtility.delete_product(merchant, event['id'])
