from django.shortcuts import render
from ecapp.models import course
# Create your views here.
def display(request):
    ec_list=course.objects.all()
    my_dict={'ec_list':ec_list}
    return render(request,'courinpt.html',context=my_dict)