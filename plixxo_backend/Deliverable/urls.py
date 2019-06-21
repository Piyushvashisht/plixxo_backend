from rest_framework import routers
from Deliverable.api import DeliverableViewSet

router = routers.DefaultRouter()
router.register('', DeliverableViewSet, 'deliverable')

urlpatterns = router.urls
