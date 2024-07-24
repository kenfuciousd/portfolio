from django.shortcuts import render, get_object_or_404, redirect
from .models import Package, Delivery, CustomUser, Post
from django.http import HttpResponseForbidden
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import login, logout
from .forms import UserRegistrationForm
import logging

def is_courier(user):
    return user.role == 'courier'

def is_client(user):
    return user.role == 'client'

def is_admin(user):
    return user.is_superuser

def is_vendor(user):
    return user.role == 'vendor'

def index(request):
    posts = Post.objects.all()
    return render(request, 'mydjangoapp/index.html', {'posts': posts})

def home(request):
    return render(request, 'mydjangoapp/home.html')

def blog(request):
    posts = Post.objects.all()
    return render(request, 'mydjangoapp/blog.html', {'posts': posts})

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    users = CustomUser.objects.all()
    packages = Package.objects.all()
    deliveries = Delivery.objects.all()
    return render(request, 'mydjangoapp/admin_dashboard.html', {'users': users, 'packages': packages, 'deliveries': deliveries})

@login_required
@user_passes_test(is_courier)
def courier_dashboard(request):
    deliveries = Delivery.objects.filter(courier=request.user)
    return render(request, 'mydjangoapp/courier_dashboard.html', {'deliveries': deliveries})

@login_required
@user_passes_test(is_vendor)
def vendor_dashboard(request):
    packages = Package.objects.filter(vendor=request.user)
    return render(request, 'mydjangoapp/vendor_dashboard.html', {'packages': packages})

@login_required
@user_passes_test(is_client)
def catalog(request):
    packages = Package.objects.filter(status='available')
    return render(request, 'mydjangoapp/catalog.html', {'packages': packages})

@login_required
@user_passes_test(is_admin)
def help_desk(request):
    transactions = Delivery.objects.all()
    return render(request, 'mydjangoapp/help_desk.html', {'transactions': transactions})

def blog(request):
    posts = Post.objects.all()
    return render(request, 'mydjangoapp/blog.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'mydjangoapp/post_detail.html', {'post': post})

def basic_auth_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Invalid login credentials')
    return render(request, 'mydjangoapp/basic_auth_login.html')

@login_required
def basic_auth_logout(request):
    logout(request)
    return redirect('login')