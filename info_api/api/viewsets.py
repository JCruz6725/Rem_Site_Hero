from info_api.models import Person, Resume
from  .serializers import PersonSerializer, ResumeSerializer
from rest_framework import viewsets

class PersonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class ResumeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
