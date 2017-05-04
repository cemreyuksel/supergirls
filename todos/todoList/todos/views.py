# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

from . models import Todo

def index(request):
  todos = Todo.objects.all()[:10]

  context = {
    'todos': todos
  }
  return render(request, 'index.html', context)
# Create your views here.

def details(request,id):
  todo = Todo.objects.get(id=id)

  context = {
    'todo': todo
  }
  return render(request, 'details.html', context)

def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        deadline = request.POST.get('deadline')
        procent = request.POST['procent']

        todo = Todo(title=title, deadline = deadline, procent=procent)
        todo.save()

        return redirect('/todos')
    else:
        return render(request, 'add.html')
