from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'common.html')

def register(request):
    return render(request,'register.html')