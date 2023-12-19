from .celery import app as celery_app

# This is the code that will be executed when celery worker is started
__all__ = ("celery_app",)

# It will load DJANGO_SETTINGS_MODULE and then autodiscover(autodiscover_tasks) all the tasks in the installed_apps
