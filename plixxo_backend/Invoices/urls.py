from rest_framework import routers
from Invoices.api import InvoicesViewSet

router = routers.DefaultRouter()
router.register('', InvoicesViewSet, 'invoices')
urlpatterns = router.urls
