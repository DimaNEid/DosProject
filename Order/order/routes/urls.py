from rest_framework import routers

from order.controllers.orderController import orderController

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'purchase', orderController, basename='purchase')

urlpatterns = router.urls