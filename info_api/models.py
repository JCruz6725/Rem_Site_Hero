from django.db import models

#refer to DB ralation diagram for full explination

class Person (models.Model):
    full_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    location = models.CharField(max_length=64)


class Resume (models.Model):
    person_email = models.ForeignKey(Person, related_name='resume', on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    summary = models.CharField(max_length=1024)
    programming_skills = models.CharField(max_length=1024)
    industry_tools = models.CharField(max_length=1024)
    office_tools = models.CharField(max_length=1024)
    related_courses = models.CharField(max_length=1024)


class Education (models.Model):
    person_email = models.ForeignKey(Person, related_name='education', on_delete=models.CASCADE)
    institution_name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    degree = models.CharField(max_length=128)
    time_at = models.CharField(max_length=32)
 
 
class Project (models.Model):
    person_email = models.ForeignKey(Person, related_name='project', on_delete=models.CASCADE)
    project_name = models.CharField(max_length=32)
    title_on_project = models.CharField(max_length=32)
    tech_used = models.CharField(max_length=32)
    summary = models.CharField(max_length=1024)
 
 
class Professional (models.Model):
    person_email = models.ForeignKey(Person, related_name='professional', on_delete=models.CASCADE)
    employer_name = models.CharField(max_length=32)
    position = models.CharField(max_length=32)
    time_at = models.CharField(max_length=32)
    title_of_project = models.CharField(max_length=32)
    tech_used = models.CharField(max_length=64)
    summary = models.CharField(max_length=1024)
