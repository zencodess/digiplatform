from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, "servicemanager/home.html", {})
    
def user(request):
    return render(request, "servicemanager/user.html", {})
    
def accountmanager(request):
    return render(request, "servicemanager/manage.html", {})

def display_user(request, userId):
    text = f("Displaying user information for {}", userId)
    return HttpResponse(text)