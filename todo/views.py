from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def addTask(request):
  #print(request.POST['task'])
  task = request.POST['task']
  Task.objects.create(task=task)
  return redirect('home')
  #return HttpResponse('The form is submitted')


def markAsDone(request, pk):
  task = get_object_or_404(Task, pk=pk)
  task.is_completed = True
  task.save()
  return redirect('home')

  # return HttpResponse(task)


def markAsUnDone(request, pk):
  task = get_object_or_404(Task, pk=pk)
  task.is_completed = False
  task.save()
  return redirect('home')


def editTask(request, pk):
  single_task = get_object_or_404(Task, pk=pk)
  if request.method == 'POST':
    new_task = request.POST['task']
    single_task.task = new_task
    single_task.save()
    return redirect('home')
  else:
    context = {
      'edit_task': single_task,
    }
  return render(request, 'edit_task.html', context)


def delete_task(request, pk):
  single_task = get_object_or_404(Task, pk=pk)
  single_task.delete()

  return redirect('home')