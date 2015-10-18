from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from pirate.models import Content, Latest
from django.db import IntegrityError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def index(request):
    return redirect('/category/movie')


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
            messages.info(request, 'New post saved :P')
        except IntegrityError:
            messages.error(request, 'Error ! Title is not unique')
            return redirect(request.path)
        return redirect('/dashboard/add')
    else:
        return render(request, 'admin/add.html')


def category_content(request, category):
    content_list = Content.objects.filter(category=category).order_by('id')
    paginator = Paginator(content_list, 10)

    page = request.GET.get('page')

    try:
        contents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contents = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contents = paginator.page(paginator.num_pages)
    return render(request, 'all_posts.html', {'contents': contents})


def single_content(request, category, slug):
    content = Content.objects.get(slug=slug)
    return render(request, 'single_post.html', {'content': content})


@login_required
def content_delete(request, category, slug):
    content = Content.objects.get(slug=slug)
    content.delete()
    return redirect('/')

def contact(request):
    return render(request, 'contact.html')
