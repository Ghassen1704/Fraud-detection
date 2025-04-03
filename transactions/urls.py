from django.urls import path
from .views import FraudDetectionView, TransactionListView, TransactionDetailView,AlertsView,TransactionStatusView

urlpatterns = [
    path('fraud-detection/', FraudDetectionView.as_view(), name='fraud-detection'),
    path('fraud-detection/<int:transaction_id>/', TransactionStatusView.as_view(), name='transaction-status'),
    path('transactions/', TransactionListView.as_view(), name='transaction-list'),  # Get all transactions
    path('transactions/<int:id>/', TransactionDetailView.as_view(), name='transaction-detail'),  # Get a single transaction
    path('alerts/', AlertsView.as_view(), name='alerts'),  # NEW ALERTS ENDPOINT

]
