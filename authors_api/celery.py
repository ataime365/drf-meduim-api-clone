import os
from celery import Celery

from django.conf import settings

# TODO: change this in production
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "authors_api.settings.local")

# Celery Instance #This name 'app' will be used to refer to this instance of celery in other parts of the system
app = Celery("authors_api")

# Using a string here means the worker doesn't have to serialize the configuration object to child processes.
# The namespace argument is used to avoid clashes between the celery configuration and the django configuration
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS) #Added lambda function
