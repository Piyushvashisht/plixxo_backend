from rest_framework import viewsets, permissions
from User.models import User, UserProfile
from User.serializers import UserSerializer, UserProfileSerializer

#User Viewset

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserProfileSerializer


class LoginViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]
    