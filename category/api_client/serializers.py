from rest_framework import serializers
from category.models import Category


class CategorySeedSerializer(serializers.ModelSerializer):
    items = serializers.JSONField(required=False) 
    merchant_id = serializers.IntegerField(required=False)
    ...
    class Meta:
        model = Category 
        fields = (
            'id', 
            'parent', 'merchant_id',
            'name', 'sort_order', 'status', 'update_at',
            'metadata_title', 'metadata_description', 'metadata_url',
            'items',
            )
    
    
    def validate_items(self, value: [{}]):
        # print("field level validation: items")
        # print(value)
        res = []
        for cat in value:
            # cat['merchant'] = self.initial_data['merchant']
            ser = CategorySeedSerializer(data=cat)
            ser.is_valid(raise_exception=True)
            res.append(ser.validated_data)

        return res

    def validate(self, attrs: {}):
        # print("object level validation")
        # if attrs['parent_id'] == 0:
        #     attrs.pop('parent_id')
        return attrs
    
    def to_internal_value(self, data):
        # print("to_internal_value")

        metadata = data.pop('metadata', {})
        for key in metadata:
            data[f'metadata_{key}'] = metadata.get(key)

        return super().to_internal_value(data)
    





salla_retrieve_schem = {
        "id": 930924203,
        "parent_id": 324324542,
        
        "name": "الفساتين",
        "status": "active",
        "sort_order": 10,
        "update_at": "2023-11-14 16:45:04",
        "image": 'null',
        
        "metadata": {
            "title": 'null',
            "description": 'null',
            "url": 'null'
        },

        "urls": {
            "customer": "https://salla.sa/dev-jhnmyomat2m1nqve/الفساتين/c930924203",
            "admin": "https://s.salla.sa/categories"
        },
        "items": [
                {
                    "id": 457047431,
                    "parent_id": 874394553,
                    
                    "name": "007",
                    "status": "active",
                    "sort_order": 4,
                    "update_at": "2023-11-18 14:36:56",
                    "image": 'null',

                    "metadata": {
                        "title": 'null',
                        "description": 'null',
                        "url": 'null'
                    },
                    
                    "urls": {
                        "customer": "https://salla.sa/dev-jhnmyomat2m1nqve/007/c457047431",
                        "admin": "https://s.salla.sa/categories"
                    },
                    "items": [],
                }
            ]
    }