
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/store-event/', include("hook.urls"), name="Events"),
    path('api/products/', include("product.urls"), name="Products"),
    path('api/categories/', include("category.urls"), name="Products"),
]

