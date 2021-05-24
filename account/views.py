from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
# Create your views here.

def index(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    return render(request, 'account/homepage.html')


''' LoginViewController '''
def loginView(request):

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'account/login.html')

    return render(request, 'account/login.html')

def signUp(request):
    return render(request, 'account/signup.html')

def logOut(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
