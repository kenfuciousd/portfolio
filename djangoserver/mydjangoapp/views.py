# views.py
from django.shortcuts import render, get_object_or_404
from .models import Package, Delivery, User, Post
from django.views.decorators.csrf import csrf_protect


def index(request):
    posts = Post.objects.all()
    return render(request, 'mydjangoapp/index.html', {'posts': posts})

def package_list(request):
    packages = Package.objects.all()
    return render(request, 'myapp/package_list.html', {'packages': packages})

def package_detail(request, package_id):
    package = get_object_or_404(Package, package_id=package_id)
    return render(request, 'myapp/package_detail.html', {'package': package})

def create_delivery(request):
    if request.method == 'POST':
        # Process the form data
        # ...
        pass
    return render(request, 'myapp/create_delivery.html')

@permission_required('myapp.view_package', raise_exception=True)
def package_detail(request, package_id):
    # Your view logic
    pass

#Cross Site Scripting Protection 
@csrf_protect
def create_delivery(request):
    # Your view logic
    pass
