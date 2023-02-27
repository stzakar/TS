from django.shortcuts import render

from .models import Task


def index(request):
    template = 'tasks/index.html'
    task_list = Task.objects.all()
    context = {
        'task_list': task_list
    }
    return render(request, template, context)
