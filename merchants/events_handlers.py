import json
from event.event_handlers.base import BaseEventHandler

from .models import Merchant
from .serializers import MerchantTokenSerialiser, MerchantSerializer
from .utils import MerchantUtility



class StoreAuthorizeHandler(BaseEventHandler):
    name = "StoreAauthorizeHandler"
    serializer = None
    

    def handle(self, merchant_id, event_data): 
        print(f"proccessing: {self.event_base}.{self.event_path}")
        

        merchant = MerchantUtility.get_or_create_merchant(merchant_id=merchant_id)
        tokens = MerchantUtility.update_or_create_tokens(
                    merchant=merchant,
                    access_token=event_data["access_token"],
                    refresh_token=event_data["refresh_token"],
                    expires=event_data["expires"],
                )

        # populate products database
        # run in other threed 
        

        MerchantUtility.populate_database(merchant_id, tokens.access_token)

        return True
    




