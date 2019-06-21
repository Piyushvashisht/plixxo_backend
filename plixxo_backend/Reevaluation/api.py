from rest_framework import viewsets, permissions
from Reevaluation.models import Reevaluation
from Reevaluation.serializers import ReevaluationSerializer

#Reevaluation Viewset

class ReevaluationViewSet(viewsets.ModelViewSet):
    queryset = Reevaluation.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ReevaluationSerializer
