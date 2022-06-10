from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin



from .models import Person, Resume, Education, Project, Professional, Account

class AccountAdmin (BaseUserAdmin):
    list_display = ('email', 'username', 'date_joined',  'is_admin')
    search_fields = ('email')
    readonly_fields = ('data_joined', 'last_login')


    list_filter = ()
    fieldsets = ()
    filter_horizontal = ()

    

admin.site.register(Account, AccountAdmin)

admin.site.register(Person)
admin.site.register(Resume)
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(Professional)

