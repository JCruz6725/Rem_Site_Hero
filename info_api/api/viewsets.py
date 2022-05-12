from info_api.models import *
from  .serializers import *
from rest_framework import viewsets

class PersonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class ResumeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

class EducationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


