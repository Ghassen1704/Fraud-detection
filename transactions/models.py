from django.db import models

class Transaction(models.Model):
    user_id = models.IntegerField()
    amount = models.FloatField()
    transaction_type = models.CharField(max_length=50)  # 'withdrawal', 'deposit', etc.
    timestamp = models.DateTimeField(auto_now_add=True)
    is_fraud = models.BooleanField(default=False)

    def __str__(self):
        return f'Transaction {self.id} by User {self.user_id}'

class Alert(models.Model):
    transaction_id = models.IntegerField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Alert for Transaction {self.transaction_id}"