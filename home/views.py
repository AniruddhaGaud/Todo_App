from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    context = {}
    if request.method == "POST":
        todo_title = request.POST.get('todo_title')
        Todo.objects.create(todo_name=todo_title)
        print(todo_title)
        return redirect('/')
    context['todos']  = Todo.objects.all()
    return render(request,'home.html',context)

def delete_todo(request,id):
    try:
        todo_obj = Todo.objects.get(id=id).delete()
    except Exception as e:
        print(e)
    return redirect('/')

def update_todo(request):
    id = request.GET.get('id')
    try:
        todo_obj = Todo.objects.get(id=id)
        todo_obj.is_completed = not todo_obj.is_completed
        todo_obj.save()
    except Exception as e:
        print(e)
    return redirect('/')
