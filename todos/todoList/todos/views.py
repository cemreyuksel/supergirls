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

def edit(request, id):
  todo = Todo.objects.get(id=id)

  context = {
    'todo': todo
  }
  if(request.method == 'POST'):
    todo.title = request.POST['title']
    todo.deadline = request.POST.get('deadline')
    todo.procent = request.POST['procent']
    todo.save()

    return redirect('/todos')
  else:
    return render(request, 'edit.html', context)

def delete(request, id):
  todo = Todo.objects.get(id=id)
  todo.delete()

  return redirect('/todos')

def impressum(request):
  return render(request, 'impressum.html')


