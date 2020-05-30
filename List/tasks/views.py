from django.shortcuts import render, get_object_or_404,redirect
from django.core.paginator import Paginator
from tasks.models import Task
from .forms import TaskForm
import datetime
from django.utils.dateformat import DateFormat

def index(request):
    list_tasks = Task.objects.all()
    paginator = Paginator(list_tasks,5)
    page = request.GET.get('page')
    task = paginator.get_page(page)


    return render(request,'tasks/list.html',{'task':task})

def add(request):
    if(request.method == 'POST'):
        
        form = TaskForm(request.POST)
        
        if (form.is_valid()):
            task = form.save(commit=False)
            task.save()
            return redirect(index)
        
    else:
        form = TaskForm()
    return render(request,'tasks/add.html',{'form':form})

def edit(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if(request.method == 'POST'):
        form = TaskForm(request.POST,instance=task)
        if(form.is_valid()):
            task.save()
            return redirect(index)
        else:
         return render(request, 'tasks/edit.html',{'form':form, 'task':task})

    else:
         return render(request, 'tasks/edit.html',{'form':form, 'task':task})

def delete(request,id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    return redirect('/')

def delete_all(request):
    task = Task.objects.all()
    task.delete()
    return redirect('/')

