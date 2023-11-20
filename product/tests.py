from django.test import TestCase
# Create your tests here.
from rest_framework import serializers  
from django.db import models




class ProductModel(models.Model):
    name = models.CharField(max_length=255)
    price_amount = serializers.IntegerField(default=0)
    price_currency = models.CharField(max_length=3, default="USD")


class ProductCreateSerializer(serializers.ModelSerializer):
    price = serializers.DictField()

    class Meta:
        model = ProductModel
        fields = ['name', 'price', 'price_amount']

    def validate(self, attrs: {}):
        price = attrs.pop('price')
        attrs['price_amount'] = price['amount']
        attrs['price_currency'] = price['currency']
        return attrs



class ProductRetriveSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    class Meta:
        model = ProductModel
        fields = ['name', 'price']

    def get_price(self, obj):
        return {
            'amount': obj.price_amount,
            'currency': obj.price_currency,
        }




data_dict = {
    'name': "test",
    'price': {
        'amount': 100,
        'currency': 'EGP'
    }
}

ser = ProductCreateSerializer(data=data_dict)
if not ser.is_valid():
    print(ser.errors) 
print(
    'on create', ser.validated_data
)

prod = ProductModel()
prod.name = "test"
prod.price_amount = 100
prod.price_currency = 'EGP'

ser = ProductRetriveSerializer(instance=prod)

print(
    'on retrieve', ser.data
)



print()