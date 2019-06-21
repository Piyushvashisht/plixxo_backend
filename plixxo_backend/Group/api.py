from rest_framework import viewsets, permissions
from Group.models import Group
from Group.serializers import GroupSerializer

#Group Viewset

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = GroupSerializer
