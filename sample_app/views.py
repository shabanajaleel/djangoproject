from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,'home.html')

def Sample(request):
     return render(request,'sample.html')