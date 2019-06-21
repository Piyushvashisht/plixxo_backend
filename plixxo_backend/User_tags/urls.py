from rest_framework import routers
from User_tags.api import User_tagsViewSet

router = routers.DefaultRouter()
router.register('', User_tagsViewSet, 'user_tags')

urlpatterns = router.urls
