from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User

# Register your models here.

class UserAdmin(BaseUserAdmin):
    """Most of these below are just customization i.e changing the defaults of the BaseUserAdmin"""
    ordering = ['email']
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    list_display = ['pkid', 'id', 'email', 'first_name', 'last_name', 'is_staff', 'is_active']
    list_display_links = ['pkid','id', 'email'] #we want the id and email to be clickable on the Admin page
    list_filter = ['email', 'is_staff', 'is_active'] #, 'first_name', 'last_name'

    # fieldsets helps us customize how different parts of our admin dashboard will look like
    #A tuple of tuples #CustomUserChangeForm #form
    fieldsets =(
        (
            _("Login Credentials"), { "fields": ("email", "password",) },
        ),
        (
            _("Personal Information"), { "fields": ("first_name", "last_name",) },
        ),
        (
            _("Permissions and Groups"), { "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions",) },
        ),
        (
            _("Important Dates"), { "fields": ("last_login", "date_joined",)},
        ),
    )

    add_fieldsets = (
        ( None , { "classes":("wide", ), #This wide class causes the fieldsets to take uo the field width of the change form
                  "fields": ("email", "first_name", "last_name", "password1", "password2"),},
                  ),
    )

    search_fields = ["email", "first_name", "last_name"]


admin.site.register(User, UserAdmin) #register the User model class using the UserAdmin customizations

