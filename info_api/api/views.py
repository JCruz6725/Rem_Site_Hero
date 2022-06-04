
from django.http import HttpResponse, JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.permissions import AllowAny



from info_api.models import Person
from django.contrib.auth.models import User
from .serializers import PersonSerializer, UserSerializer


class UserList(APIView):
    permission_classes = [AllowAny]
    #permission_classes = [IsAuthenticated]

    def get(self, request, format=None):

        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data[0])

#class ProjectList(APIView):


