from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.
def home(request):

    return render(request,'home.html',{"users":User.objects.all()})

def room(request,room_name):
    return render(request,'room.html',{"roomname":room_name,"users":User.objects.all()})

# code for login user ----------------------------------------------------
def Log_in(request):
    if request.method=="POST":
        username=request.POST.get('username')
        # username="admin"
        password=request.POST.get('password')
        # password="admin"
        user=authenticate(username=username,password=password)
        login(request,user)
        return redirect('/')
    return redirect('/')

# code for sign up user-------------------------------------------
def sign_up(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if password == cpassword:
            myuser=User.objects.create_user(username=username,password=password)
            # myuser.set_password(password)
            myuser.save()

            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('/')

        else:
            return redirect('/')
    return redirect('/')


# code for logout user ----------------------------------------------------
def Log_out(request):
    if request.method=="POST":
        logout(request)
    return redirect('/')
