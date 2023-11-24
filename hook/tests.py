


from hook.serialiserzes import WebhookPayloadSerializer
from .event_handlers import EventMapper


event = {
    "event":"app.store.authorize",
    # "event":"product.updated",
    # "event":"category.created",
    "merchant": 1234918345,
    "created_at": "2021-10-05 16:41:07",
    "data": {
        "access_token": "kG7eCGY0QlrgNZK1zFQmRIifReqsKJ9GJquPvsnJhho.l5Msr8jD5GBxxxx",
        "expires": 1634661667,
        "refresh_token": "WYQz6bMeaonMZ6WjhrkMTRb7fSkrAVpLH5n1V0_X9eU.e5Gqz1ks8Q8dHxxxx",
        "scope": "settings.read offline_access",
        "token_type": "bearer"
    }
} 

# SIMULATING WEBHOOK ENDPOINT
serializer = WebhookPayloadSerializer(data=event)
serializer.is_valid(raise_exception=True)

event = serializer.validated_data.get("event")
merchant = serializer.validated_data.get("merchant")
data = serializer.validated_data.get("data")


event_handler = EventMapper.get_event_handler(event) # object
if event_handler:
    succsess = event_handler.MerchantUtility(merchant, data)
    if succsess:
        print(f"handled: {succsess}") 


# # from .serialiserzes import WebhookPayloadSerializer

# # print(repr(WebhookPayloadSerializer()))


