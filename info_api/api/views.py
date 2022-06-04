
from django.http import HttpResponse, JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.permissions import AllowAny



from info_api.models import Person
from .serializers import PersonSerializer


class PersonList(APIView):
    permission_classes = [AllowAny]
    #permission_classes = [IsAuthenticated]

    def get(self, request, format=None):

        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data[1])

#class ProjectList(APIView):


