

from django.shortcuts import render, redirect
from django.utils.timezone import now
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'todo/index.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        if title:
            Task.objects.create(title=title)
        return redirect('index')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.completed_at = now()
    task.points = 10  # Reward points for task completion
    task.save()
    return render(request, 'todo/completed.html', {'task': task})

