from django.http import request
from django.shortcuts import render , redirect
#from . models import Book,Category
from .forms import UserRegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import  messages 
from django.contrib import  auth
from dashboard.models import Homehowork , Todo
from django.contrib.auth.decorators  import  login_required 

# Create your views here.


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('index')    



def singup_page(request):
    register_form = UserRegistrationForm()
    if request.method == 'POST':
        register_form = UserRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.info(request, 'Account Created Succefully')
            return redirect('login')        
    context={
        'register_form':register_form
    }        
    return render(request ,'accountes/singup.html', context )



def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = auth.authenticate(request , username=username , password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index') 
        else:
            messages.info(request , 'Invalid Credentaisl')    
    context = {

    }
    return render(request ,'accountes/login.html', context ) 


@login_required
def profile(request):
    homeworks = Homehowork.objects.filter(is_finished=False, user=request.user)
    todos = Todo.objects.filter(is_finished=False, user=request.user)
    if len(homeworks) == 0:
        homework_done = True
    else:
        homework_done = False
    if len(todos) == 0:
        todos_done = True
    else:
        todos_done = False
    context = {
        'homeworks': homeworks,
        'todos':todos,
        'homework_done':homework_done,
        'todos_done':todos_done,

    }
    return render(request, 'accountes/profil.html' , context)