from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from todo.models import Task


def index(request):
	if request.method == 'POST':
	  Task.objects.create(name=request.POST['task_name'])

	return render(request,"todolist/index.html") 
