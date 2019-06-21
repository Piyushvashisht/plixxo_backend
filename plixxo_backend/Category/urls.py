from rest_framework import routers
from Category.api import CategoryViewSet

router = routers.DefaultRouter()
router.register('', CategoryViewSet, 'category')

urlpatterns = router.urls
