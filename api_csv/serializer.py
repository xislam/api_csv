from rest_framework import serializers
from rest_framework.serializers import Serializer, FileField

# Serializers define the API representation.
from api_csv.models import User, Gem, Transaction


class UploadSerializer(Serializer):
    file_uploaded = FileField()

    class Meta:
        fields = ['file_uploaded']


class UsersSerializer(serializers.ModelSerializer):
    customer = serializers.CharField(source='username')

    class Meta:
        model = User
        fields = ['customer']


class GemSerializer(serializers.ModelSerializer):
    item = serializers.CharField(source='text')

    class Meta:
        model = Gem
        fields = ['item']


class TransactionSerializer(serializers.ModelSerializer):
    customer = serializers.CharField(source='customer.username')
    item = serializers.CharField(source='item.text')

    class Meta:
        model = Transaction
        fields = ['customer', 'item', 'total', 'quantity', 'date']
