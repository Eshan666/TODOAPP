from django.shortcuts import render, redirect
from CRUD.models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib import messages

# Create your views here.

@login_required(login_url = "loginPage")
def home(request):
    context = {}
    print(request.user)
    if request.method == 'POST':
        user = request.POST.get('user')
        note = request.POST.get('note')
        task = Task(user=user, note=note)
        task.save()
    
    tasks = Task.objects.all()
    context={"tasks" : tasks}
    return render(request, 'CRUD/home.html',context)


@login_required(login_url = "loginPage")
def update(request):
     return render(request, 'CRUD/update.html')


@login_required(login_url = "loginPage")
def delete_item(request, pk):

    obj = Task.objects.get(id=pk)
    context = {"obj": obj}
    if request.method == "POST":
        obj.delete()
        return redirect('/')
    return render(request, 'CRUD/delete.html', context)

@login_required(login_url = "loginPage")
def update_item(request,pk):
    item = Task.objects.get(id=pk)
    
    
    context = {"item":item}

    if request.method == "POST":
        user = request.POST.get('user')
        note = request.POST.get('note')
        item.user = user
        item.note = note
        item.save()         
      

    return render(request,"CRUD/update.html",context)


def registerPage(request):
     if request.user.is_authenticated:
        return redirect('home')
     else:

        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():

                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account has been created for '+ user)
                return redirect('loginPage')

        context = {"form" : form}


        return render(request,"CRUD/register.html",context)



def loginPage(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    else:

        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user =  authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,"username or password is incorrect")

    return render(request,"CRUD/login.html")

    
    

def logoutPage(request):
    logout(request)
    return redirect('loginPage')

