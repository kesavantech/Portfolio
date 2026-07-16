from django.contrib import admin

# Register your models here.

from .models import Portfolio, Skill, Project

admin.site.register(Portfolio)
admin.site.register(Skill)
admin.site.register(Project)

