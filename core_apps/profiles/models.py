from django.db import models
from django.contrib.auth import get_user_model #Returns the active User model , current logged in user
from django.utils.translation import gettext_lazy as _ 
from django_countries.fields import CountryField #A country field for Django models that provides all countries as choices.
from phonenumber_field.modelfields import PhoneNumberField
from core_apps.common.models import TimeStampedUUIDModel

# Create your models here.

User = get_user_model()

class Gender(models.TextChoices):
    """TextChoices is a way to create a group of choices for model fields"""
    MALE = "M", _("Male") #string representation
    FEMALE = "F", _("Female") #string representation
    OTHER = "O", _("Other") #string representation


class Profile(TimeStampedUUIDModel):
    """
    Inheriting from TimeStampedUUIDModel enables use id, pkid,created_at and updated_at from the base class, 
    without defining it again.
    """
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE) #one user to one profile
    phone_number = PhoneNumberField(verbose_name=_("Phone Number"), max_length=30, default="+2348068975326")
    about_me = models.TextField(verbose_name=_("About me"), default="say something about yourself")
    gender = models.CharField(verbose_name=_("Gender"), choices=Gender.choices, default=Gender.OTHER, max_length=20)
    country = CountryField(verbose_name=_("Country"), default="NG", blank=False, null=False) #cant be blank or null
    city = models.CharField(verbose_name=_("City"), max_length=180, default="Lagos", blank=False ,null=False)
    profile_photo = models.ImageField(verbose_name=_("Profile Photo"), default="/profile_default.png")
    twitter_handle = models.CharField(verbose_name=_("twitter handle"), max_length=20, blank=True)
    followers = models.ManyToManyField( #becomes a list
        "self", symmetrical=False, related_name="following", blank=True) #symmetrical=False (Not Reciprocal) e.g follows, not friendships
#profile_followers
    def __str__(self):
        return f"{self.user.first_name}'s Profile"
    
    def follow(self, profile):
        """This is possible because of the ManyToManyField 'self' relationship.
        profile here is another profile instance I want to follow ...... Django Abstraction"""
        self.followers.add(profile)

    def unfollow(self, profile):
        """This is possible because of the ManyToManyField and 'self' relationship """
        self.followers.remove(profile)

    def check_following(self, profile):
        return self.followers.filter(pkid=profile.pkid).exists()


 