from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request, 'others/home.html', {})

def register(request):
    return render(request, 'registration/registration.html', {})

def login_view(request):
    return render(request, 'registration/login.html', {})
