from django.urls import path
from . import views  # Import views from the current directory

urlpatterns = [
    path('', views.home, name='home'),  # This should be the home view
    path('packages/<int:package_id>/', views.package_detail, name='package_detail'),
    path('create_delivery/', views.create_delivery, name='create_delivery'),
    path('update_delivery_status/<int:delivery_id>/', views.update_delivery_status, name='update_delivery_status'),
    path('register/', views.register, name='register'),
    path('login/', views.basic_auth_login, name='basic_auth_login'),
]