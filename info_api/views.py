#from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from Rem_Site_Hero.info_api.mySerializers import *


class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Person.objects.all().order_by('-date_joined')
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticated]

