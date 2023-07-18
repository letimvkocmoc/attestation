from rest_framework import serializers
from retail_network.models import *


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class RetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = RetailNetwork
        fields = '__all__'
