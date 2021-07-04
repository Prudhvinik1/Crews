from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import render

def index(request):
    return render(request,'clubs/login.html',{})

def signup(request):
    return render(request,'clubs/registration.html',{})

def createUser(request):
    if request.method == 'POST':
        username = request.POST.get('userName')
        email = request.POST.get('emailId')
        password = request.POST.get('password')
        user = User.objects.create_user(username,email,password)
        user.save()
        return HttpResponse("User with username {} created".format(username))

def changePassword(request):
    u = User.objects.get(username='prudhvi')
    u.set_password('pru@123')
    u.save()

def login(request):
    if request.method == 'POST':
        username = request.POST.get('userName')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        if user is not None:
            #Authenticated
            return HttpResponse('User Authenticated')
        else:
            #Not Authenticated
            return HttpResponse('User Not Authenticated')
