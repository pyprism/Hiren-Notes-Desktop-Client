from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from pirate.models import Content, Latest
from django.db import IntegrityError
# Create your views here.


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
        try:
            obj = Content(title=request.POST['title'], content=request.POST['content'],
                      category=request.POST['select'])
            obj.save()
            Latest(reference=obj).save()
        except IntegrityError:
            messages.error(request, 'Error ! Title is not unique')
            return redirect(request.path)
        return redirect('/dashboard/add')
    else:
        return render(request, 'admin/add.html')

