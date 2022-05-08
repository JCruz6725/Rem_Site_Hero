from rest_framework import serializers 
#from api.models import *


class PersonSerializer (serializers.Serializer):
    full_name = serializers.CharField(required=True, allow_blank=False, max_length=32)
    email = serializers.CharField(required=True, allow_blank=False, max_length=32)


class ResumeSerializer (serializers.Serializer):
    person_email = PersonSerializer(many=True, read_only=True)
    title = serializers.CharField(required=True, allow_blank=False, max_length=32)
    summary = serializers.CharField(required=True, allow_blank=False, max_length=512)
    skills = serializers.CharField(required=True, allow_blank=False, max_length=512)
    related_courses = serializers.CharField(required=True, allow_blank=False, max_length=512)


class Education (serializers.Serializer):
    person_email = PersonSerializer(many=True, read_only=True)
    institution_name = serializers.CharField(required=True, allow_blank=False, max_length=32)
    degree = serializers.CharField(required=True, allow_blank=False, max_length=32)
    time_at = serializers.CharField(required=True, allow_blank=False, max_length=32)
 
 
class Project (serializers.Serializer):
    person_email = PersonSerializer(many=True, read_only=True)
    #Change...
    #resume_title = models.ForeignKey(Resume, on_delete=models.CASCADE)
    project_name = serializers.CharField(required=True, allow_blank=False, max_length=32)
    title_on_project = serializers.CharField(required=True, allow_blank=False, max_length=32)
    tech_used = serializers.CharField(required=True, allow_blank=False, max_length=32)
    summary = serializers.CharField(required=True, allow_blank=False, max_length=512)
 
 
class Professional (serializers.Serializer):
    person_email = PersonSerializer(many=True, read_only=True)
    #Change...
    #resume_title  = models.ForeignKey(Resume, on_delete=models.CASCADE)
    employer_name = serializers.CharField(required=True, allow_blank=False, max_length=32)
    time_at = serializers.CharField(required=True, allow_blank=False, max_length=32)
    title_on_project = serializers.CharField(required=True, allow_blank=False, max_length=32)
    tech_used = serializers.CharField(required=True, allow_blank=False, max_length=32)
    summary = serializers.CharField(required=True, allow_blank=False, max_length=512)