from django.shortcuts import render, redirect
from todo.models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from todo.forms import SignUpForm



@login_required(login_url='/login/')
def home_view(request):
    tasks = Task.objects.filter(user=request.user, is_completed=False).order_by('-updated_at')  # Decanding order
    
    # tasks = Task.objects.filter(is_completed=False).order_by('updated_at')  # Assending order
    # print(tasks)

    completed_tasks = Task.objects.filter(is_completed=True)
    
    context = {'tasks':tasks, 'completed_tasks':completed_tasks}

    return render(request, 'testapp/home.html', context)

# Signup
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password']) # Password encrypt karne ke liye
            user.save()
            login(request, user) # Register hote hi login ho jayega
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'testapp/signup.html', {'form': form})

# Login View
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'testapp/login.html', {'form': form})

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')



@login_required(login_url='login') # Bina login ke koi task add na kar paye
def addTask(request):
    if request.method == 'POST':
        task_text = request.POST.get('task')
        
        # Task ko database mein save karne se pehle current logged-in user se jodein
        new_task = Task(task=task_text, user=request.user) 
        new_task.save()
        
        return redirect('home')


