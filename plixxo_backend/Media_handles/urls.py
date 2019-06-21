from rest_framework import routers
from Media_handles.api import Media_handlesViewSet

router = routers.DefaultRouter()
router.register('', Media_handlesViewSet, 'media_handles')

urlpatterns = router.urls
