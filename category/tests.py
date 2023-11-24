from django.test import TestCase

# Create your tests here.
from .serializers import CategorySeedSerializer

ser = CategorySeedSerializer(
            data={
                'id': 32432,
                'items': [
                    {
                        'id': 646734
                    }
                ],
                'metadata':{
                    'title': "rter"
                }
            }
        )
ser.is_valid(raise_exception=True)

# print(type(ser.validated_data))
# print(ser.validated_data)

