import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _ #This works when Django translation system is enabled, helps us translate the string into different languages
from .managers import CustomUserManager 


class User(AbstractBaseUser, PermissionsMixin):
    """AbstractBaseUser doesnt have fields pre-defined, sso we have to define the fields by ourself.
    pseudo primary key, to solve the disadvantages of using uuid as the main primary key id. """
    pkid = models.BigAutoField(primary_key=True, editable=False) 
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    # first_name = models.CharField(_("first name"), max_length=150, blank=True) #default from AbstractUser
    first_name = models.CharField(verbose_name=_('First Name'), max_length=50) #Verbose is useful for admin interface and the documentation generator.
    last_name = models.CharField(verbose_name=_('Last Name'), max_length=50)
    email = models.EmailField(verbose_name=_('Email Address'), db_index=True,  unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    #This USERNAME_FIELD is used as the unique identifier for authentication, using email as username
    USERNAME_FIELD = "email" 
    REQUIRED_FIELDS = ["first_name", "last_name"] #when creating createsuperuser or user

    # Using the custom user manager we created, for queries
    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User") #Verbose is useful for admin interface and the documentation generator.
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.first_name

    @property
    def get_full_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"
    
    @property
    def get_short_name(self):
        return self.first_name
    

