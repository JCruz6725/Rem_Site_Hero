from rest_framework import serializers 
from info_api.models import *




class ResumeSerializer (serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = "__all__"


class EducationSerializer (serializers.Serializer):
    class Meta:
        model = Education
        fields = "__all__"


class ProjectSerializer (serializers.Serializer):
    class Meta:
        model = Project
        fields = "__all__"


class ProfessionalSerializer (serializers.Serializer):
    class Meta:
        model = Professional
        fields = "__all__"



class PersonSerializer (serializers.ModelSerializer):
    resume = ResumeSerializer(many = True, read_only=True)
    education = EducationSerializer(many=True, read_only=True)
    project = ProjectSerializer(many=True, read_only=True)
    class Meta: 
        model = Person
        fields = "__all__"



 
 




