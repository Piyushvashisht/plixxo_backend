from rest_framework import viewsets, permissions
from Deliverable.models import Deliverable
from Deliverable.serializers import DeliverableSerializer

#Deliverable Viewset

class DeliverableViewSet(viewsets.ModelViewSet):
    queryset = Deliverable.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DeliverableSerializer
