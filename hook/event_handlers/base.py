
class BaseEventHandler:
    name = "BaseEventHandler"
    serializer = None
    modle = None
    
    event_base = None
    event_path = None

    def __init__(self, event_base, event_path):
        self.event_base = event_base
        self.event_path = event_path

        
    def handle_event(self, merchant, event_data): 
        if self.event_path:
            # print(self.event_path)
            if hasattr(self, self.event_path):
                return getattr(self, self.event_path)(merchant, event_data)
        
        return self.handle(merchant, event_data)
    
    def handle(self, merchant, event_data):
        return False






        



