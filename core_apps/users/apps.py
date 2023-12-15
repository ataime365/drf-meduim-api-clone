from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _ #For translation to other languages  #Internationalization


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.users"
    verbose_name = _("Users") # Translation #singular
