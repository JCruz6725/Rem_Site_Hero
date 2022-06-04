from rest_framework import serializers 
from info_api.models import *




class ResumeSerializer (serializers.ModelSerializer):
    user = serializers.CharField(source=("user.email"))
    class Meta:
        model = Resume
        fields = "__all__"


class EducationSerializer (serializers.ModelSerializer):
    #user_email = serializers.CharField(source=("user.email"))
    class Meta:
        model = Education
        fields = "__all__"


class ProjectSerializer (serializers.ModelSerializer):
    user_email = serializers.CharField(source=("user.email"))
    class Meta:
        model = Project
        fields = "__all__"


class ProfessionalSerializer (serializers.ModelSerializer):
    user_email = serializers.CharField(source=("user.email"))
    class Meta:
        model = Professional
        fields = "__all__"


class PersonSerializer (serializers.ModelSerializer):
    user = serializers.CharField(source=("user.email"))
    class Meta: 
        model = Person
        fields = "__all__"


class UserSerializer (serializers.ModelSerializer):
    person = PersonSerializer(many=True, read_only=True)
    resume = ResumeSerializer(many=True, read_only=True)
    education = EducationSerializer(many=True, read_only=True)
    project = ProjectSerializer(many=True, read_only=True)
    professional = ProfessionalSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'education', 'resume', 'project', 'professional', 'person']


 
 




