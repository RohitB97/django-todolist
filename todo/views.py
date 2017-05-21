from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Task


def index(request):
	task_list = Task.objects.all();
	context = {'task_list':task_list}
	return render(request,"todo/index.html",context)

def detail(request,task_id):
    task = Task.objects.get(pk=task_id)
    context = {'task':task}
    return render(request,"todo/detail.html",context)    

