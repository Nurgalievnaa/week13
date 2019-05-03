from django.contrib import admin
from api.models import TaskList
from api.models import Task

admin.site.register(TaskList)
admin.site.register(Task)


# Register your models here.
