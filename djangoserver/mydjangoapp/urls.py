from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:post_id>/', views.post_detail, name='post_detail'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('courier_dashboard/', views.courier_dashboard, name='courier_dashboard'),
    path('vendor_dashboard/', views.vendor_dashboard, name='vendor_dashboard'),
    path('catalog/', views.catalog, name='catalog'),
    path('help_desk/', views.help_desk, name='help_desk'),
    path('login/', views.basic_auth_login, name='basic_auth_login'),
    path('logout/', views.basic_auth_logout, name='basic_auth_logout'),
#    path('register/', views.register, name='register'),
]

#urlpatterns = [
#    path('', views.index, name='index'),
#    path('blog/', views.blog, name='blog'),
#    path('admin_page/', views.admin_page, name='admin_page'),
#    path('catalog/', views.catalog, name='catalog'),
#    path('vendor/', views.vendor_page, name='vendor_page'),
#    path('help_desk/', views.help_desk, name='help_desk'),
#    path('login/', views.basic_auth_login, name='basic_auth_login'),
#    path('home/', views.home, name='home'),  # Adjusted to use the correct view
#    path('packages/', views.package_list, name='package_list'),
#    path('packages/<int:package_id>/', views.package_detail, name='package_detail'),
#    path('create_delivery/', views.create_delivery, name='create_delivery'),
#    path('update_delivery_status/<int:delivery_id>/', views.update_delivery_status, name='update_delivery_status'),
#    path('register/', views.register, name='register'),
#]