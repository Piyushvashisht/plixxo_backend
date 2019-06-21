from rest_framework import viewsets, permissions
from Kyc.models import Kyc
from Kyc.serializers import KycSerializer

#Kyc Viewset

class KycViewSet(viewsets.ModelViewSet):
    queryset = Kyc.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = KycSerializer
