from email import message
from django.shortcuts import render, redirect 
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse 
from loginapp.models import login 
from loginapp import forms
def login(request):
    if request.method=='POST':
        username= request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username)
        
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid credentials!")
            return redirect('register')

    else: 
        return render(request,'login.html')
