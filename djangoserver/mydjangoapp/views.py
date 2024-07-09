from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'myapp/index.html', {'posts': posts})