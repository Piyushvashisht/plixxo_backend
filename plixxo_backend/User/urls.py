from rest_framework import routers
from User.api import UserViewSet, LoginViewSet

router = routers.DefaultRouter()
router.register('', UserViewSet, 'users')
#router.register('login/', LoginViewSet, 'user_login')

urlpatterns = router.urls
