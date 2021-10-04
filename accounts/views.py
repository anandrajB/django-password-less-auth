from django.contrib import auth
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from accounts.forms import MyCustomuserForm

# Create your views here.


def index(request):
    return render(request,'index.html')



def RegisterPage(request):
    if request.method == "POST":
        form  = MyCustomuserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"user created successfully")
            return redirect('register')

    else:
        f = MyCustomuserForm()
    return render(request,'register.html',{'form':f})


def LoginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")

        user = authenticate(request , username = username)
        if user is not None:
            login(request,user)
            return redirect('home')

        else:
            messages.info(request,"user doesn't exist ")

    context = {}
    return render(request,'login.html',context)        



