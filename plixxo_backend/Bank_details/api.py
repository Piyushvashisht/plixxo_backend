from rest_framework import viewsets, permissions
from Bank_details.models import Bank_details
from Bank_details.serializers import Bank_detailsSerializer

#Bank_details Viewset

class Bank_detailsViewSet(viewsets.ModelViewSet):
    queryset = Bank_details.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Bank_detailsSerializer
