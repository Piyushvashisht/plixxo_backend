from rest_framework import routers
from Kyc.api import KycViewSet

router = routers.DefaultRouter()
router.register('', KycViewSet, 'kyc')

urlpatterns = router.urls
