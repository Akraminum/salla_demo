from rest_framework import serializers

from merchants.models import Merchant, MerchantToken

class MerchantTokenSerialiser(serializers.ModelSerializer):
    class Meta:
        model = MerchantToken
        fields = '__all__'

class MerchantSerializer(serializers.ModelSerializer):
    token = MerchantToken()
    
    class Meta:
        model = Merchant
        fields = '__all__'