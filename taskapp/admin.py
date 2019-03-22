from django.contrib import admin

# Register your models here.
from taskapp.models import Task

admin.site.register(Task)
