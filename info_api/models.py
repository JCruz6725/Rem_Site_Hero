from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager

#refer to DB ralation diagram for full explination

class AccountManager (BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError ("email is required")
            
        if not username:
            raise ValueError ("username is required")

        new_account = self.model(email=self.normalized_email(email), username=username)
        new_account.set_password(password)
        new_account.save(using=self._db)
        return new_account

    def create_superuser(self, email, username, password=None):
        new_account = self.create_user(email, username=user, password=password)

        new_account.is_admin = True
        new_account.is_superuser =True
        new_account.is_staff =True
        
        new_account.save(using=self._db)
        return new_account


class Account (AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=63, unique=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    last_login = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = AccountManager()
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Person (models.Model):
    user = models.ForeignKey(User, related_name='person',on_delete=models.CASCADE)
    #full_name = models.CharField(max_length=64)
    #email = models.CharField(max_length=64)
    location = models.CharField(max_length=64)

    def __str__(self):
        return self.user
    



class Resume (models.Model):
    user_email = models.ForeignKey(User, related_name='resume', on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    summary = models.CharField(max_length=1024)
    programming_skills = models.CharField(max_length=1024)
    industry_tools = models.CharField(max_length=1024)
    office_tools = models.CharField(max_length=1024)
    related_courses = models.CharField(max_length=1024)
    
    def __str__(self):
        return self.title
    


class Education (models.Model):
    user_email = models.ForeignKey(User, related_name='education', on_delete=models.CASCADE)
    institution_name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    degree = models.CharField(max_length=128)
    time_at = models.CharField(max_length=32)

    def __str__(self):
        return self.institution_name
    


class Project (models.Model):
    user_email = models.ForeignKey(User, related_name='project', on_delete=models.CASCADE)
    project_name = models.CharField(max_length=32, default='')
    title_on_project = models.CharField(max_length=32, default='')
    tech_used = models.CharField(max_length=32, default='')
    summary = models.CharField(max_length=1024, default='')

    def __str__(self):
        return self.project_name
    


class Professional (models.Model):
    user_email = models.ForeignKey(User, related_name='professional', on_delete=models.CASCADE)
    employer_name = models.CharField(max_length=32)
    position = models.CharField(max_length=32)
    time_at = models.CharField(max_length=32)
    title_of_project = models.CharField(max_length=32)
    tech_used = models.CharField(max_length=64)
    summary = models.CharField(max_length=1024)

    def __str__(self):
        return self.title_of_project
    
