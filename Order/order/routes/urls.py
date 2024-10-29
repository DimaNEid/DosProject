from rest_framework import routers
from order.controllers.PurchaseController import PurchaseController

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'purchase', PurchaseController, basename='purchase')

urlpatterns = router.urls