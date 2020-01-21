from django.shortcuts import render
from django.utils import timezone
# Create your views here.
from . import models
from django.http import HttpResponseRedirect


def home(request):
    todo_items = models.Todo.objects.all().order_by('-added_date')
    stuff_for_frontend = {
        'todo_items': todo_items,
    }
    return render(request, 'my_app/index.html', stuff_for_frontend)


def add_todo(request):
    content = request.POST.get('content')
    current_date = timezone.now()
    models.Todo.objects.create(added_date=current_date, text=content)
    return HttpResponseRedirect("/")


def delete_todo(request, todo_id):
    delete = models.Todo.objects.get(id=todo_id)
    delete.delete()
    return HttpResponseRedirect("/")