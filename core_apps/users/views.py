from .serializers import UserSerializer
from rest_framework.generics import RetrieveUpdateAPIView #used on just a single model instance
from rest_framework.permissions import IsAuthenticated #Allows access only to authenticated users
from django.contrib.auth import get_user_model #Return the User model that is active in this project


class CustomUserDetailsView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,) #Allows access only to authenticated users

    def get_object(self):
        return self.request.user
    
    def get_queryset(self):
        return get_user_model().objects.none()
