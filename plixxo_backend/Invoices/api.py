from rest_framework import viewsets, permissions
from Invoices.models import Invoices
from Invoices.serializers import InvoicesSerializer
from User.models import User

#Invoices Viewset

class InvoicesViewSet(viewsets.ModelViewSet):
    queryset = Invoices.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = InvoicesSerializer
    
