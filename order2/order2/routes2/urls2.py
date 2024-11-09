from rest_framework import routers
from order2.controllers2.PurchaseController2 import PurchaseController2

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'purchase2', PurchaseController2, basename='purchase2')

urlpatterns = router.urls

print(router.urls)

