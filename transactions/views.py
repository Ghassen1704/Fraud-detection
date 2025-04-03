import joblib
from django.http import JsonResponse
from django.views import View
from .models import Transaction,Alert
from .serializers import TransactionSerializer
from django.views.decorators.csrf import csrf_exempt
import json

# Load the trained model
model = joblib.load("ml/fraud_model.pkl")

from .tasks import analyze_transaction

class FraudDetectionView(View):
    @csrf_exempt
    def post(self, request):
        try:
            # Parse the JSON data from the request body
            request_data = json.loads(request.body)
            print("Request received:", request_data)  # Print the request data for debugging
            
            # Serialize the data
            serializer = TransactionSerializer(data=request_data)
            if serializer.is_valid():
                transaction = serializer.save()
                
                # Run the fraud detection task in the background
                analyze_transaction.delay(transaction.id)  # Celery task
                
                # Respond with the transaction id and message
                return JsonResponse({
                    'message': 'Transaction processing started.',
                    'transaction_id': transaction.id
                })
            else:
                return JsonResponse(serializer.errors, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

class TransactionStatusView(View):
    def get(self, request, transaction_id):
        try:
            transaction = Transaction.objects.get(id=transaction_id)
            return JsonResponse({
                'transaction_id': transaction.id,
                'is_fraud': transaction.is_fraud
            })
        except Transaction.DoesNotExist:
            return JsonResponse({'error': 'Transaction not found'}, status=404)
        
class TransactionListView(View):
    """Returns all transactions (fraud & normal)"""
    def get(self, request):
        transactions = list(Transaction.objects.values())  # Get all transactions
        return JsonResponse(transactions, safe=False)  # Return as JSON

class TransactionDetailView(View):
    """Returns details of a specific transaction"""
    def get(self, request, id):
        try:
            transaction = Transaction.objects.get(id=id)
            return JsonResponse({
                "id": transaction.id,
                "amount": transaction.amount,
                "status": transaction.status,
                "timestamp": transaction.timestamp
            })
        except Transaction.DoesNotExist:
            return JsonResponse({"error": "Transaction not found"}, status=404)
        
class AlertsView(View):
    """Returns a list of fraud alerts"""
    def get(self, request):
        alerts = list(Alert.objects.values())  # Get all alerts from the DB
        return JsonResponse(alerts, safe=False)