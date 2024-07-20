# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Package, Delivery, User, Post
from django.http import HttpResponseForbidden
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import login
from .forms import UserRegistrationForm
import logging


def is_courier(user):
    return user.role == 'courier'

def is_client(user):
    return user.role == 'client'

def index(request):
    posts = Post.objects.all()
    return render(request, 'mydjangoapp/index.html', {'posts': posts})

@login_required
def package_list(request):
    packages = Package.objects.all()
    return render(request, 'mydjangoapp/package_list.html', {'packages': packages})

#def package_detail(request, package_id):
#    package = get_object_or_404(Package, package_id=package_id)
#    return render(request, 'mydjangoapp/package_detail.html', {'package': package})

@login_required
def package_detail(request, package_id):
    package = get_object_or_404(Package, package_id=package_id)
    if not request.user.is_authenticated or (request.user.role == 'client' and package.client != request.user):
        return HttpResponseForbidden("You are not allowed to view this package.")
    deliveries = Delivery.objects.filter(package=package)
    return render(request, 'mydjangoapp/package_detail.html', {'package': package, 'deliveries': deliveries})

@login_required
@user_passes_test(is_client)
@csrf_protect
def create_delivery(request):
    if request.method == 'POST':
        package_id = request.POST.get('package_id')
        courier = request.POST.get('courier')
        client = request.POST.get('client') # user_id?
        pickup_location = request.POST.get('pickup_location')
        dropoff_location = request.POST.get('dropoff_location')
        delivery_status = request.POST.get('delivery_status')

        package = get_object_or_404(Package, package_id=package_id)
        courier = get_object_or_404(User, user_id=courier)
        client = get_object_or_404(User, user_id=client)

        delivery = Delivery.objects.create(
            package=package,
            courier=courier,
            client=client,
            pickup_location=pickup_location,
            dropoff_location=dropoff_location,
            delivery_status=delivery_status,
        )

        logger.info(f"Delivery created: {delivery.delivery_id} by user: {request.user.id}")
        return redirect('package_detail', package_id=package_id)

    packages = Package.objects.all()
    couriers = User.objects.filter(role='courier')
    clients = User.objects.filter(role='client')
    return render(request, 'mydjangoapp/create_delivery.html', {
        'packages': packages,
        'couriers': couriers,
        'clients': clients,
    })

@login_required
@user_passes_test(is_courier)
def update_delivery_status(request, delivery_id):
    delivery = get_object_or_404(Delivery, delivery_id=delivery_id)
    if request.method == 'POST':
        delivery_status = request.POST.get('delivery_status')
        delivery.delivery_status = delivery_status
        delivery.save()
        return redirect('package_detail', package_id=delivery.package.package_id)

    return render(request, 'mydjangoapp/update_delivery_status.html', {'delivery': delivery})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to a home page or any other page
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def home(request):
    return render(request, 'mydjangoapp/index.html')

def index(request):
    posts = Post.objects.all()
    return render(request, 'mydjangoapp/index.html', {'posts': posts})

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
    return render(request, 'basic_auth_login.html')

#@permission_required('mydjangoapp.view_package', raise_exception=True)
#def package_detail(request, package_id):
    # Your view logic
#    pass

#Cross Site Scripting Protection 
#@csrf_protect
#def create_delivery(request):
    # Your view logic
#    pass

@login_required
@user_passes_test(is_courier)
def courier_dashboard(request):
    # Courier-specific logic
    pass

@login_required
@user_passes_test(is_client)
def client_dashboard(request):
    # Client-specific logic
    pass