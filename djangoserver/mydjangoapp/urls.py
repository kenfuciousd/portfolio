from django.urls import path
from . import views  # Import views from the current directory

urlpatterns = [
    path('', views.index, name='index'),
]