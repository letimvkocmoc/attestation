from rest_framework import serializers
from sole_trader.models import *


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class SoleTraderSerializer(serializers.ModelSerializer):

    class Meta:
        model = SoleTrader
        fields = '__all__'
