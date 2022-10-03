from django.shortcuts import render

# Create your views here.

def home(request):
     return render(request,'schooltemplates/home.html'),
def viewstaff(request):
     return render(request,'schooltemplates/viewstaff.html')     
