from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'bootapp/index.html')

def home2(request):
    return render(request, 'bootapp/index-2.html')
