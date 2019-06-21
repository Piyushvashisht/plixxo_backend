from rest_framework import viewsets, permissions
from Campaign_content.models import Campaign_content
from Campaign_content.serializers import Campaign_contentSerializer

#Campaign_content Viewset

class Campaign_contentViewSet(viewsets.ModelViewSet):
    queryset = Campaign_content.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Campaign_contentSerializer
