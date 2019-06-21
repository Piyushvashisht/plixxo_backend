from rest_framework import viewsets, permissions
from Media_handles.models import Media_handles
from Media_handles.serializers import Media_handlesSerializer

#Media_handles Viewset

class Media_handlesViewSet(viewsets.ModelViewSet):
    queryset = Media_handles.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Media_handlesSerializer
