from celery import shared_task
import joblib
from .models import Transaction

model = joblib.load("ml/fraud_model.pkl")

@shared_task
def analyze_transaction(transaction_id):
    transaction = Transaction.objects.get(id=transaction_id)
    features = [[transaction.amount, 1 if transaction.transaction_type == 'withdrawal' else 0]]
    
    prediction = model.predict(features)
    transaction.is_fraud = prediction[0] == -1
    transaction.save()
