from rest_framework import routers
from Reevaluation.api import ReevaluationViewSet

router = routers.DefaultRouter()
router.register('', ReevaluationViewSet, 'reevaluation')

urlpatterns = router.urls
