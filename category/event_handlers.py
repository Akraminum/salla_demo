from event.event_handlers.base import BaseEventHandler


class CategoryEventHandler(BaseEventHandler):
    name = "ProductEventHandler"
    serializer = None

    def created(self, merchant, event):
        print('******** logic *********')        
        print(f"merchant_id: {merchant}")
        print('**************************')
        return True
    
    def updated(self, merchant, event):
        print('******** logic *********')
        print(f"merchant_id: {merchant}")
        print('**************************')
        return True
    
    def deleted(self, merchant, event):
        ...
        print('******** logic *********')
        print(f"merchant_id: {merchant}")
        print('**************************')
        return True
