from rest_framework import routers
from User.api import UserProfileViewSet

router = routers.DefaultRouter()
router.register('', UserProfileViewSet, 'users')
#router.register('login/', LoginViewSet, 'user_login')

urlpatterns = router.urls