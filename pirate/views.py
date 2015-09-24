from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template import RequestContext


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('/dashboard')
        else:
            messages.error(request, 'Username/Password is not valid!')
            return redirect(request.path)
    else:
        return render(request, 'admin/login.html')


def logout(request):
    auth.logout(request)
    return redirect("/login")


@login_required
def dashboard(request):
    return render(request, 'admin/dashboard.html')


@login_required
def add(request):
    if request.method == 'POST':
        print(request.POST.get('content'))
        print(request.POST.get('select'))
        return redirect('/dashboard/add')
    else:
        return render(request, 'admin/add.html')




