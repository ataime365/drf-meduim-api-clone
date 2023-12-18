from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

# from .models import User
from django.contrib.auth import get_user_model #Return the User model that is active in this project.

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    """Custom form for user creation, extending the default UserCreationForm"""
    class Meta(UserCreationForm.Meta): #Added .Meta
        model = User
        fields = ["first_name", "last_name", "email"]
        # error_class = "error"

    error_messages = {
        "duplicate_email": "A user with this email already exists.",
    }
    
    def clean_email(self):
        """ We will then override the default clean email method to check if the email already exists"""
        email = self.cleaned_data["email"] #cleaned_data is a dictionary
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return 
        raise forms.ValidationError(self.error_messages['duplicate_email'])


class CustomUserChangeForm(UserChangeForm):
    """Custom form for user modification"""
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ["first_name", "last_name", "email"]
        error_class = "error"