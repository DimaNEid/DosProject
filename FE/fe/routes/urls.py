
from rest_framework.routers import SimpleRouter

from fe.controllers.InfoController import InfoController
from fe.controllers.PurchaseController import PurchaseController
from fe.controllers.SearchController import SearchController

router = SimpleRouter(trailing_slash=False)

router.register(r'info', InfoController, basename='info' )
router.register(r'search', SearchController, basename='search' )
router.register(r'purchase', PurchaseController, basename='purchase' )

urlpatterns = router.urls