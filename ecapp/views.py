from django.shortcuts import render
from ecapp.models import course
from django.urls import reverse
from django.template import Context, loader
from django.http import HttpResponse,HttpResponseRedirect
from ecapp import forms
# Create your views here.
def display(request):
    ec_list=course.objects.all()
    my_dict={'ec_list':ec_list}
    return render(request,'courdly.html',context=my_dict)
def cinpt(request):    
    form=forms.ceform()
    if request.method=='POST':
        form=forms.ceform(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
    return render(request,'courinpt.html',{'form':form})
def search(request):
    if request.method=="POST":
        searched=request.POST['searched']
        course=course.objects.filter(Coursename_contains=searched)

        return render(request,'search_result.html',{'searched':searched,'course':course})
    else:
        return render(request,'search_result.html',{})  
def cartadd(request):
    ec_list=course.objects.all()
    my_dict={'ec_list':ec_list}
    return render(request,'cart.html',context=my_dict)  