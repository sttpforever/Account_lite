from django.contrib import admin

from .models import MyUser, Project, Customer, Bank, Check

admin.site.register(Project)
admin.site.register(Customer)
admin.site.register(Bank)
admin.site.register(Check)
admin.site.register(MyUser)
