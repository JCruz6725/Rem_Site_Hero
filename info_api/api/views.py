from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

#from .serializers import UserSerializer, ProjectSerializer
from info_api.api.serializers import (AccountSerializer, 
                                    ResumeSerializer, 
                                    ProjectSerializer, 
                                    EducationSerializer, 
                                    ProfessionalSerializer,
                                    ProfileSerializer )

from info_api.models import Resume, Project, Professional, Education
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

##################################################
### For Current user to get/post/update/delete ###
##################################################

class UserResumeList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        resume = Resume.objects.filter(account_email=request.user)
        serializer = ResumeSerializer(resume, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        account = Account.objects.get(email=request.user)
        resume = Resume.objects.create(account_email=account)
        serializer = ResumeSerializer(resume, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProjectList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        project = Project.objects.filter(account_email=request.user)
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        account = Account.objects.get(email=request.user)
        project = Project.objects.create(account_email=account)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserEducationList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        education = Education.objects.filter(account_email=request.user)
        serializer = EducationSerializer(education, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        account = Account.objects.get(email=request.user)
        education = Education.objects.create(account_email=account)
        serializer = EducationSerializer(education, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfessionalList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        professional = Professional.objects.filter(account_email=request.user)
        serializer = ProfessionalSerializer(professional, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        account = Account.objects.get(email=request.user)
        professional = Professional.objects.create(account_email=account)
        serializer = ProfessionalSerializer(professional, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    permission_classes = [AllowAny]

    def get_account_object(self, email):
        try:
            return Account.objects.get(email=email)
        except Account.DoesNotExist:
            raise Http404

    def get_resume_object(self, title):
        try:
            return Resume.objects.get(title=title)
        except Resume.DoesNotExist:
            raise Http404

    def get(self, request, email, format=None):
        account = self.get_account_object(email)
        serializer = ProfileSerializer(account)
        return Response(serializer.data)