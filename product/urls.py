
from django.urls import path
from .views import ProductViewSet
from rest_framework import routers
from django.urls import include

router = routers.DefaultRouter()
router.register('', ProductViewSet)

urlpatterns = [
    path('', include(router.urls))
]



# from .tests import *