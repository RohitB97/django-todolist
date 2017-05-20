from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request, "todo/views/index.html")

def detail(request, task_id):
    return render(request,"todo/views/detail.html",{'task_id':task_id})    

