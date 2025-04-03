import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fraud_detection.settings')

app = Celery('fraud_detection')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatically discover tasks in Django apps
app.autodiscover_tasks()

# Update Celery configuration for Windows compatibility
app.conf.update(
    worker_pool='solo',  # Use solo pool for Windows compatibility
)
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fraud_detection.settings')

app = Celery('fraud_detection')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatically discover tasks in Django apps
app.autodiscover_tasks()

# Update Celery configuration for Windows compatibility
app.conf.update(
    worker_pool='solo',  # Use solo pool for Windows compatibility
)
