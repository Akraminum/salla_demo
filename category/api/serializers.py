from rest_framework import serializers
from category.models import Category


class CategoryViewOutputSerializer(serializers.ModelSerializer):
    ...
    # parent_id is parent.id
    parent_id = serializers.IntegerField(read_only=True)

    # chiled items
    subs = serializers.SerializerMethodField()
    metadata = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = (
            'id', 'parent_id',
            'name', 'sort_order', 'status', 'update_at',
            'metadata',  'subs'
            )
    
    def get_subs(self, obj):
        return CategoryViewOutputSerializer(obj.subs, many=True).data

    def get_metadata(self, obj):
        return {
            'title': obj.metadata_title,
            'description': obj.metadata_description,
            'url': obj.metadata_url
        }
        
