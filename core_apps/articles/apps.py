from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _ #For translation to other languages  #Internationalization

class ArticlesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.articles"
    verbose_name = _("Articles") # Translation #singular
    
    def ready(self):
        import core_apps.search.signals

