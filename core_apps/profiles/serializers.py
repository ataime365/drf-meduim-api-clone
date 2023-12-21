from django_countries.serializer_fields import CountryField
from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name") # one-to-one field
    last_name = serializers.CharField(source="user.last_name") # one-to-one field
    email = serializers.CharField(source="user.email") # one-to-one field

    full_name = serializers.SerializerMethodField(read_only=True) # Custom field
    profile_photo = serializers.SerializerMethodField() # For further customizations
    country = CountryField(name_only=True)

    class Meta:
        model = Profile
        fields = ["id", "first_name", "last_name","full_name", "email", "profile_photo","phone_number", 
                  "gender", "country", "about_me", "city", "twitter_handle"]
        
    
    def get_full_name(self, obj): #obj here is the Profile object
        first_name = obj.user.first_name.title()
        last_name = obj.user.last_name.title()
        return f"{first_name} {last_name}"
    
    def get_profile_photo(self, obj): #obj here is the Profile object
        return obj.profile_photo.url
    
    
# Here we specify the fields we want the user to be able to update
class UpdateProfileSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)

    class Meta:
        model = Profile
        fields = ["profile_photo","phone_number", # Here we specify the fields we want the user to be able to Update
                  "gender", "country", "about_me", "city", "twitter_handle"]
        

# The serializer we want to use for the users following this profile #using this for that view
class FollowingSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name") # one-to-one field
    last_name = serializers.CharField(source="user.last_name") # one-to-one field

    class Meta:
        model = Profile
        fields = ["first_name", "last_name", #For the followers, this are the fields we want to see
                  "profile_photo", "about_me","twitter_handle"]


