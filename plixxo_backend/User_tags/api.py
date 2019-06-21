from rest_framework import viewsets, permissions
from User_tags.models import User_tags
from User_tags.serializers import User_tagsSerializer

#User_tags Viewset

class User_tagsViewSet(viewsets.ModelViewSet):
    queryset = User_tags.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = User_tagsSerializer
