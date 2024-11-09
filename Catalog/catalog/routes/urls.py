from django.core.serializers import serialize
from rest_framework_nested import routers
from sqlalchemy import false

from catalog.controllers.searchController import searchController
from catalog.controllers.infoController import infoController
from catalog.controllers.updateController import updateController

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'search', searchController, basename='search')
router.register(r'info', infoController, basename='info')
router.register(r'update', updateController, basename='update')

urlpatterns = router.urls


