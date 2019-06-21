from rest_framework import routers
from Campaign.api import CampaignViewSet


router = routers.DefaultRouter()
router.register('', CampaignViewSet, 'campaign')

urlpatterns = router.urls
