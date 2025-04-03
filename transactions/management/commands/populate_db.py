import random
from faker import Faker
from django.core.management.base import BaseCommand
from transactions.models import Transaction, Alert  # Import your models

fake = Faker()

class Command(BaseCommand):
    help = "Populate the database with fake transactions and fraud alerts"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Generating fake transactions..."))

        # Create 50 fake transactions
        for _ in range(50):
            amount = round(random.uniform(10.0, 5000.0), 2)  # Random amount
            card_number = fake.credit_card_number()
            user_id = random.randint(1, 1000)  # Random user_id, assuming user IDs range from 1 to 1000
            transaction_type = random.choice(['withdrawal', 'deposit'])  # Random transaction type
            is_fraud = random.choice([True, False])  # Randomly mark fraud cases

            transaction = Transaction.objects.create(
                user_id=user_id,
                amount=amount,
                transaction_type=transaction_type,
                is_fraud=is_fraud
            )

            # If fraud detected, create an alert
            if is_fraud:
                Alert.objects.create(
                    transaction_id=transaction.id,
                    message=f"Suspicious transaction detected: {amount} USD"
                )

        self.stdout.write(self.style.SUCCESS("Database populated successfully!"))
