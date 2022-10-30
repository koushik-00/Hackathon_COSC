from email import message
from django.shortcuts import render, redirect 
from django.contrib import messages
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth.models import User
from loginapp.models import login 
from signupapp import forms
from loginapp import forms
from signupapp.models import details
def login(request):
    form=forms.loForm()
    if request.method=='POST':
        form=forms.loForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
    return render(request,'login.html',{'form':form})

     