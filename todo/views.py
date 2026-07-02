from django.shortcuts import render, redirect, get_object_or_404
from todo.models import Task
from django.contrib.auth.decorators import login_required

# Create your views / business logic here 👇.

# 1. Add Task
@login_required(login_url='login')
def addTask(request):  
    if request.method == 'POST':
        task = request.POST['task']
        if task:
        # Current logged-in user ke sath task save ho raha hai
            Task.objects.create(task=task, user=request.user)
    return redirect('home')


# 2. Mark as done (Sirf apna task hi done kar sake)
@login_required(login_url='login')
def mark_as_done(request, pk):  # Mark as done
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.is_completed = True
    task.save()
    return redirect('home')


# 3. Mark as undone
@login_required(login_url='login')
def mark_as_undone(request, pk):  
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')


# 4. Edit Task
@login_required(login_url='login')
def edit_task(request, pk):  
    get_task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        new_task = request.POST.get('task')
        if new_task:
            get_task.task = new_task
            get_task.save()
            return redirect('home')
    else:
        context = {'get_task': get_task}
    return render(request, 'testapp/edit_task.html', context)


# 5. Delete Task
@login_required(login_url='/login/')
def delete_task(request, pk):  # Delete Task
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    return redirect('home')

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from todo.serializers import TaskSerializer
# Create & See Records 

class TaskListCreateAPIView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Retrive Update & Destroy

class TaskListRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'