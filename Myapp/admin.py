from django.contrib import admin

# Register your models here.

from .models import Portfolio, Skill, Project, Employee, Education

admin.site.register(Portfolio)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Employee)
admin.site.register(Education)

