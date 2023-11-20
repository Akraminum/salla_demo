
from event.event_handlers.base import BaseEventHandler
from .register_handlers import r

class EventMapper:

    handlers = r
    
    def __init__(self):
        ...

    @classmethod
    def register_handler(cls, event_type:str, handler:BaseEventHandler):
        cls.handlers[event_type] = handler

    @classmethod
    def get_event_list(cls):
        return list(cls.handlers.keys())

    @classmethod
    def get_event_handler(cls, event: str):
        # order.products.updated

        event_parts = event.split('.')
        for i in range(len(event_parts), 0, -1):
            event_base = '.'.join(event_parts[:i])
            # print(event)
            handler = cls.handlers.get(event_base, None)
            if handler:
                return handler(event_base = event_base, event_path = '_'.join(event_parts[i:]))

        
        # raise Exception("Invalid Event Name")
        return None