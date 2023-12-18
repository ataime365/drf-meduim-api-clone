from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    This would be used in objects in the user model, A model must have a manager, default manager is always objects, but objects can be changed
    """
    
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_('You must provide a valid email address'))
        

    def create_user(self, first_name, last_name, email, password, **extra_fields):
        """I dont need username here"""

        
        if not first_name:
            """Checks"""
            raise ValueError(_('Users must submit a first name'))

        if not last_name:
            """Checks"""
            raise ValueError(_('Users must submit a last name'))
        
        if email:
            email = self.normalize_email(email) #Normalize the email address by lowercasing the domain part of it.
            self.email_validator(email)
        else:
            raise ValueError(_("User must have an email address"))
        

        user = self.model(first_name=first_name, 
                          last_name=last_name, 
                          email=email,
                          **extra_fields)
        
        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user.save(using=self._db) #This is used the save the user object to the database
        return user
    
    def create_superuser(self, first_name, last_name, email, password, **extra_fields):
        """Overriding the default django create_superuser to also accept an email as a parameter
        """
        extra_fields.setdefault("is_staff", True) #This are the things that make it a superuser
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            """Checks"""
            raise ValueError(_("Superusers must have is_staff=True"))

        if extra_fields.get("is_superuser") is not True:
            """Checks"""
            raise ValueError(_("Superusers must have is_superuser=True"))

        if not password:
            raise ValueError(_("Superusers must have a password"))
        
        if email:
            email = self.normalize_email(email) #Normalize the email address by lowercasing the domain part of it.
            self.email_validator(email)
        else:
            raise ValueError(_('Superuser must have an email address'))

        user = self.create_user(first_name, last_name, email, password,
                          **extra_fields)
        
        user.save(using=self._db)
        return user
    
