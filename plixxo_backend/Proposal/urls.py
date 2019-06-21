from rest_framework import routers
from Proposal.api import ProposalViewSet

router = routers.DefaultRouter()
router.register('', ProposalViewSet, 'proposal')

urlpatterns = router.urls
