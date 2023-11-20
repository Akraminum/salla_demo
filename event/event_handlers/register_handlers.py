
from category.event_handlers import CategoryEventHandler
from merchants.events_handlers import StoreAuthorizeHandler
from product.event_handlers import ProductEventHandler


r = {
    "category": CategoryEventHandler,
    "product": ProductEventHandler,
    "app.store.authorize": StoreAuthorizeHandler
}
