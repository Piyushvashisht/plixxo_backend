from rest_framework import viewsets, permissions
from Campaign.models import Campaign
from Campaign.serializers import CampaignSerializer

#Campaign Viewset

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CampaignSerializer
