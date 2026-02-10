from django.shortcuts import render

# from myproject import firstapp

# Create your views here.

def home(request):
    return render(request, 'firstapp/index.html' )
