from django import forms

class TaskForm(forms.Form):
    task_name = forms.CharField(label='Enter your task', max_length=100)