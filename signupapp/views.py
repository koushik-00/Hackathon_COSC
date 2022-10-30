
from signupapp import forms
from email import message
from django.shortcuts import render, redirect 
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User, auth
from django.http import HttpResponse 
from signupapp.models import details
# Create your views here.
def register(request):
    form=forms.DetailsForm()
    if request.method=='POST':
        form=forms.DetailsForm(request.POST,request.FILES)
        if form.is_valid():
            p1=request.POST.get('Password')
            p2=request.POST.get('ConfirmPassword')
            em=request.POST.get('Email')
            if p1==p2:
                 if details.objects.filter(Email=em).exists():
                    messages.error(request,'user already exists') 
                 else:
                    form.save(commit=True)
            else:
                messages.error(request,'passwords do not match')
    return render(request,'register.html',{'form':form})

def login(request):
    '''form=forms.loForm()
    if request.method=='POST':
        form=forms.loForm(request.POST,request.FILES)
        username=request.POST.get('Email')
        password=request.POST.get('Password')
        user = authenticate(request,Email=request.POST.get('Email'),Password=request.POST.get('Password'))
        if user is not None:
            login(request,user)
            return redirect('home')

    context = {}
    print('username or password incorrect')
    return render(request,'login.html',context)'''
        
    form=forms.loForm()
    if request.method=='':
        form=forms.loForm(request.POST)
        if form.is_valid():
            username=request.POST.get('Email')
            password=request.POST.get('Password')
            user=authenticate(request,username,password)
            if details.objects.filter(Email=username).exists() and details.objects.filter(Password=password).exists():
                message.success(request,'login successful')
            else:
                message.error(request,'wrong email or password')
    return render(request,'login.html',{'form':form})