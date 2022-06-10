from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Person, Resume, Education, Project, Professional, Account

admin.site.register(Account, UserAdmin)

admin.site.register(Person)
admin.site.register(Resume)
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(Professional)

