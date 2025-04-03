# fraud_detection/transactions/serializers.py
from rest_framework import serializers
from .models import Transaction,Alert

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
class AlertSerializer(serializers.ModelSerializer):
    transaction = TransactionSerializer(read_only=True)

    class Meta:
        model = Alert
        fields = '__all__'