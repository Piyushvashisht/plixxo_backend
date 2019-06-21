from rest_framework import viewsets, permissions
from Platform.models import Platform
from Platform.serializers import PlatformSerializer

class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PlatformSerializer
    