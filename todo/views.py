from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

from django.http import HttpResponse
from .models import Task


def index(request):
	task_list = Task.objects.all()
	context = {'task_list':task_list}
	return render(request,"todo/index.html",context)

def detail(request,id):
	if request.method == 'POST':
		temp = Task.objects.get(id=id)
		temp.name = request.POST['task_edit_name']
		temp.save()
		return redirect("index")
	else :
		task = Task.objects.get(id=id)
		context = {'task':task}
		return render(request,"todo/detail.html",context)

def delete(request, id):
	if request.method == 'POST':
		temp = Task.objects.get(id=id)
		temp.delete()
		return redirect("index")

