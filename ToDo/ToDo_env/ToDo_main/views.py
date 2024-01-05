from django.shortcuts import render
from ToDoApp.models import Task
def home(request):
    tasks=Task.objects.filter(is_completed=False).order_by('-updated_on')
    completed_task=Task.objects.filter(is_completed=True).order_by('-updated_on')
    
    

    context={
        'tasks':tasks,
        'completed_task': completed_task
    }
    return render(request,'home_page.html',context)