from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'description', 'created_at', 'deadline', 'author'
        )


admin.site.register(Task, TaskAdmin)
