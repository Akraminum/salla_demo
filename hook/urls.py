from django.urls import path
from .views import EventAPIView

urlpatterns = [
    path('', EventAPIView.as_view()),
]




# from .tests import * 