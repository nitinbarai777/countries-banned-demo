from rest_framework import routers
from countrybanned.core.views import *


router = routers.DefaultRouter()


# Core
router.register('countries', CountryViewSet, basename='countries')
