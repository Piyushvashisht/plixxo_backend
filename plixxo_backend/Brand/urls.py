from rest_framework import routers
from Brand.api import BrandViewSet

router = routers.DefaultRouter()
router.register('', BrandViewSet, 'brands')

urlpatterns = router.urls
