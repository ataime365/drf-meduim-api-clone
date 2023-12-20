from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from dj_rest_auth.views import PasswordResetConfirmView
from core_apps.users.views import CustomUserDetailsView


# optional info, but good
schema_view = get_schema_view(
    info=openapi.Info(
        title="Authors Haven API",
        default_version="v1",
        description="API endpoints for Authors Haven API Course",
        contact=openapi.Contact(email="ataime15@gmail.com"),
        license=openapi.License(name="MIT License")
    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)


urlpatterns = [
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0) ), #docs
    path(settings.ADMIN_URL , admin.site.urls), # admin/ to supersecret/ #base.py
    path("api/v1/auth/user/", CustomUserDetailsView.as_view(), name="user_details"),
    path("api/v1/auth/", include("dj_rest_auth.urls")), # click on the .urls #6 endpoints
    path("api/v1/auth/registration/", include("dj_rest_auth.registration.urls")), # click on the .urls #2 endpoints
    path("api/v1/auth/password/reset/confirm/<uidb64>/<token>/", 
            PasswordResetConfirmView.as_view(), name="password_reset_confirm",),

]


# Further customization
admin.site.site_title = "Authors Haven Admin Portal"
admin.site.site_header = "Authors Haven API Admin"
admin.site.index_title = "Welcome to Authors Haven API Portal"
