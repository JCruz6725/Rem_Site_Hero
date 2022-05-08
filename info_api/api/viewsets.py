from info_api.models import Person
from  .serializers import PersonSerializer
from rest_framework import viewsets

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = SnippetSerializer