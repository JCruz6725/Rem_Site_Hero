from django.db import models

#refer to DB ralation diagram for full explination

class Person (models.Model):
    full_name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)


class Resume (models.Model):
    person_email = models.ForeignKey(Person, related_name='resume', on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    summary = models.CharField(max_length=512)
    skills = models.CharField(max_length=512)
    related_courses = models.CharField(max_length=512)


class Education (models.Model):
    person_email = models.ForeignKey(Person, related='education' on_delete=models.CASCADE)
    institution_name = models.CharField(max_length=32)
    degree = models.CharField(max_length=32)
    time_at = models.CharField(max_length=32)
 
 
class Project (models.Model):
    person_email = models.ForeignKey(Person, related_name='project' on_delete=models.CASCADE)
    # May need to change...
    #resume_title = models.ForeignKey(Resume, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=32)
    title_on_project = models.CharField(max_length=32)
    tech_used = models.CharField(max_length=32)
    summary = models.CharField(max_length=512)
 
 
class Professional (models.Model):
    person_email = models.ForeignKey(Person, related_name='professional' on_delete=models.CASCADE)
    #resume_title  = models.ForeignKey(Resume, on_delete=models.CASCADE)
    employer_name = models.CharField(max_length=32)
    time_at = models.CharField(max_length=32)
    title_on_project = models.CharField(max_length=32)
    tech_used = models.CharField(max_length=32)
    summary = models.CharField(max_length=512)
