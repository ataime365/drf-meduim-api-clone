from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _ #For translation to other languages  #Internationalization


class ProfilesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.profiles"
    verbose_name = _("Profiles") # Translation #singular
