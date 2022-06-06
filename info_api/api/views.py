
from django.http import HttpResponse, JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.permissions import AllowAny



from info_api.models import Resume, Education, Project, Professional, Person
from django.contrib.auth.models import User
from .serializers import UserSerializer, ProjectSerializer


class UserList(APIView):
    permission_classes = [AllowAny]
    #permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)


class UserDetail(APIView):
    permission_classes = [AllowAny]
    #permission_classes = [IsAuthenticated]

    def get(self, email, request, format=None):
        user = User.objects.get(email=email)
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)


class ProjectList(APIView):
    # Need to fix the permission later 
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        project = Project.objects.all()
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProjectSerializer(data=request.data)
        
        #user = request.data['user_email']
        #serializer = UserSerializer(user, many=False)
        #return Response(serializer.data)
        #serializer.data[] = user.email
        if (serializer.is_valid()):
            newPro = serializer.create(serializer.data)
            serializer.updata(newPro, serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#class ProjectList(APIView):


