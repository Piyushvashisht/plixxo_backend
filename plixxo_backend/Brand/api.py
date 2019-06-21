from rest_framework import viewsets, permissions
from Brand.models import Brand
from Brand.serializers import BrandSerializer

#Brand Viewset

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = BrandSerializer
