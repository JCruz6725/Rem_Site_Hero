from info_api.models import *
from  .serializers import *
from rest_framework import viewsets

class PersonViewSet(veiwsets.ModelViewSet):
    queryset = Person.object.all()
    serializer_class = SnippetSerializer