from rest_framework import routers
from Group.api import GroupViewSet

router = routers.DefaultRouter()
router.register('',GroupViewSet, 'group')

urlpatterns = router.urls
