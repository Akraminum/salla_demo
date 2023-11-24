from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from django.db.models import Prefetch
from django.db import connection

from category.models import Category
from .serializers import CategoryViewOutputSerializer

class CategoryListViewSet(ListModelMixin, 
                          RetrieveModelMixin,
                          GenericViewSet):
    queryset = Category.objects.all()\
        .prefetch_related(
            Prefetch(
                'subs', 
                Category.objects.all().prefetch_related("subs")
            ),
        ).filter(parent=None)
    serializer_class = CategoryViewOutputSerializer

    def get_queryset(self):
        if self.action == "retrieve":
            return self.queryset
        elif self.action == "list":
            return self.queryset.filter(parent=None)
    
    def retrieve(self, request, *args, **kwargs):
        r = super().retrieve(request, *args, **kwargs)
        [print(q) for q in connection.queries]; return r

    def list(self, request, *args, **kwargs):
        r = super().list(request, *args, **kwargs)
        [print(q) for q in connection.queries]; return r





