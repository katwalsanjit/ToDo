from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Task


def addTask(request):
  #print(request.POST['task'])
  task = request.POST['task']
  Task.objects.create(task=task)
  return redirect('home')
  #return HttpResponse('The form is submitted')
