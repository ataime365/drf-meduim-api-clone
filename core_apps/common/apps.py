from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _ #For translation to other languages  #Internationalization


class CommonConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.common"
    verbose_name = _("Common") # Translation #singular
