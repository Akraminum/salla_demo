
from django.urls import path, include
from rest_framework import routers

from .api.views import CategoryListViewSet

router = routers.DefaultRouter()
router.register('', CategoryListViewSet)

urlpatterns = [
    path('', include(router.urls))
]


# from .tests import *