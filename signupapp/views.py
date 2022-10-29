from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.
def register(request):
    if request.method=='POST':
        Name=request.POST['Name']
        Email=request.POST['Email']
        Password=request.POST['Password']
        ConfirmPassword=request.POST['ConfirmPassword']
        if Password==ConfirmPassword:
            if User.objects.filter(Email=Email).exists():
                print('Email exists')
            else:
                user=User.objects.create_user(Name=Name,Email=Email,Password=Password,ConfirmPassword=ConfirmPassword)
                user.save();
        else:
            print('password not matching')
        return redirect('/')
    else:
        return render(request,'courinpt.html')
