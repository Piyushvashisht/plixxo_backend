from rest_framework import routers
from Bank_details.api import Bank_detailsViewSet

router = routers.DefaultRouter()
router.register('', Bank_detailsViewSet, 'bank_details')

urlpatterns = router.urls
