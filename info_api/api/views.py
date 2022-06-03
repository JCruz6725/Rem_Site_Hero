from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from info_api.models import Snippet
from .serializers import PersonSerializer

@api_view(['GET', 'POST'])