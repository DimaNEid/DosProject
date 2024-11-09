from django.core.serializers import serialize
from rest_framework_nested import routers
from sqlalchemy import false

from catalog.controllers2.searchController2 import searchController2
from catalog.controllers2.infoController2 import infoController2
from catalog.controllers2.updateController2 import updateController2

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'search', searchController2, basename='search')
router.register(r'info', infoController2, basename='info')
router.register(r'update', updateController2, basename='update')

urlpatterns = router.urls




