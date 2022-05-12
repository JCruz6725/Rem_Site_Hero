from rest_framework import routers
from info_api.api.viewsets import * 

router = routers.DefaultRouter()
router.register(r'person', PersonViewSet)
router.register(r'resume', ResumeViewSet)
router.register(r'education', EducationViewSet)
