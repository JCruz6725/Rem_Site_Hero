from info_api.models import *
from  .serializers import *
from rest_framework import viewsets

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.object.all()
    serializer_class = SnippetSerializer