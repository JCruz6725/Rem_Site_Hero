from rest_framework import routers
from info_api.api.viewsets import * 

router = routers.DefaultRouter()
router.register(r'person', PersonViewSet)
