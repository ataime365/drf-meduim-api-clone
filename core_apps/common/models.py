from django.db import models
import uuid

# Create your models here.
class TimeStampedUUIDModel(models.Model):
    """
    In Django, an abstract class is a type of model that serves as a base class from which other models can inherit. 
    It is defined similarly to a regular Django model, but it does not correspond to its own database table. 
    Instead, when you create models that inherit from an abstract class, each subclass will have its own database table, 
    and the fields of the abstract class are included in these tables.
    The purpose of an abstract base class in Django is to provide a common set of fields and
    methods that can be shared across multiple models. This helps in reducing redundancy and makes your code more maintainable.
    """
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) #auto_now  updates the timestamp each time we save

    class Meta:
        """abstract = True, is what makes it an abstract class"""
        abstract = True #The model won't be created in the database, this just acts as a base class for other models
        ordering = ["-created_at", "-updated_at"]



