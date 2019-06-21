from rest_framework import viewsets, permissions
from Proposal.models import Proposal
from Proposal.serializers import ProposalSerializer

#Proposal Viewset

class ProposalViewSet(viewsets.ModelViewSet):
    queryset = Proposal.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProposalSerializer
