from rest_framework import routers
from Campaign_content.api import Campaign_contentViewSet

router = routers.DefaultRouter()
router.register('', Campaign_contentViewSet, 'campaign_content')

urlpatterns = router.urls
