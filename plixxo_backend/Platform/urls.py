from rest_framework import routers
from Platform.api import PlatformViewSet

router = routers.DefaultRouter()
router.register('', PlatformViewSet, 'platforms')

urlpatterns = router.urls
