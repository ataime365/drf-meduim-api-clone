from dj_rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from rest_framework import serializers
from django.contrib.auth import get_user_model
from django_countries.serializer_fields import CountryField
from phonenumber_field.serializerfields import PhoneNumberField

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """The reason for this is mainly because most fields arent directly on the 
        User Model, we had to get them from the profile Model"""
    """The related_name attribute (profile)  is used to create a reverse relation from the User model to the Profile model.
      This is how you would access the Profile object associated with a given User instance."""
    gender = serializers.CharField(source="profile.gender") # This is possible because of the one-to-one relationship
    phone_number = PhoneNumberField(source="profile.phone_number")
    # profile_photo = serializers.ImageField(source="profile.profile_photo")
    profile_photo = serializers.ReadOnlyField(source="profile.profile_photo.url")
    country = CountryField(source="profile.country")
    city = serializers.CharField(source="profile.city")

    # first_name = serializers.SerializerMethodField() ### SerializerMethodField is used when we want to add customization
    # last_name = serializers.SerializerMethodField()
    # full_name = serializers.SerializerMethodField(source="get_full_name")

    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name", "gender",
                  "phone_number","profile_photo","country","city"] #,"full_name"

    # def get_first_name(self, obj):
    #     """Because we used the 'SerializerMethodField' on first_name field """
    #     return obj.first_name.title()
    
    # def get_last_name(self, obj):
    #     return obj.last_name.title()
    
    def to_representation(self, instance):
        """Customizations"""
        representation = super(UserSerializer, self).to_representation(instance) # representation = data
        if instance.is_superuser:
            representation["admin"] = True
        return representation
    

class CustomRegisterSerializer(RegisterSerializer):
    username = None
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def get_cleaned_data(self):
        super().get_cleaned_data() #returns the clean data from the parent class
        return {
            "email": self.validated_data.get("email", ""),
            "first_name": self.validated_data.get("first_name", ""),
            "last_name": self.validated_data.get("last_name", ""),
            "password1": self.validated_data.get("password1", ""),
        }


    def save(self, request):
        """copied from the base class i.e RegisterSerializer """
        adapter = get_adapter() #This is used to perform the actual actions of the authentication process and create a new user
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user = adapter.save_user(request, user, self)
        user.save()
        # self.custom_signup(request, user)
        setup_user_email(request, user, [])
        # New
        user.email = self.cleaned_data.get("email")
        user.password = self.cleaned_data.get("password1")
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        return user