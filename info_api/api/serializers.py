from rest_framework import serializers 

from django.conf import settings as s

from django.contrib.auth import get_user_model
Account = get_user_model()

from info_api.models import Resume, Project, Education, Professional


#from info_api.models import Resume, Education, Project, Professional, Person
#from django.contrib.auth.models import User


class AccountSerializer (serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email', 'username', 'location']


class ResumeSerializer (serializers.ModelSerializer):
    #account_email = AccountSerializer()
    class Meta:
        model = Resume
        fields = "__all__"
        extra_kwargs = {'account_email': {'required': False}}

class ProjectSerializer (serializers.ModelSerializer):
    #user_email = serializers.CharField(source=("user_email.email"), read_only=False)
    class Meta:
        model = Project
        fields = "__all__"
        extra_kwargs = {'account_email': {'required': False}}


class EducationSerializer (serializers.ModelSerializer):
    #user_email = serializers.CharField(source=("user_email.email"))
    class Meta:
        model = Education
        fields = "__all__"
        extra_kwargs = {'account_email': {'required': False}}

class ProfessionalSerializer (serializers.ModelSerializer):
    #user_email = serializers.CharField(source=("user_email.email"))
    class Meta:
        model = Professional
        fields = "__all__"
        extra_kwargs = {'account_email': {'required': False}}
