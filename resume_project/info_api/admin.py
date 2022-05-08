from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Person)
admin.site.register(Resume)
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(Professional)

