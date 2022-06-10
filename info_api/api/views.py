
from django.http import HttpResponse, JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.permissions import AllowAny



#from info_api.models import Resume, Education, Project, Professional, Person
#from django.contrib.auth.models import User
#from .serializers import UserSerializer, ProjectSerializer
from .serializers import AccountSerializer

from django.conf import settings #for *settings.AUTH_USER_MODEL*


from django.contrib.auth import get_user_model


Account = get_user_model()


class AccountList(APIView):
    permission_classes = [AllowAny]
    #permission_classes = [IsAuthenticated]

    def get(self, request, format=None):

        account = Account.objects.all()
        serializer = AccountSerializer(account, many=True)
        return Response(serializer.data)


class AccountDetail(APIView):
    permission_classes = [AllowAny]
    #permission_classes = [IsAuthenticated]

    def get_object(self, username):
        try:
            return Account.objects.get(username=username)
        except Account.DoesNotExist:
            raise Http404



    def get(self, request, username, format=None):
        account = self.get_object(username)
        serializer = AccountSerializer(account)
        return Response(serializer.data)

'''
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
            user_instance = User.objects.get()

            new_project = Project.Create(serializer.data)

            serializer.updata(newPro, serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetail(APIView):
    pass





'''