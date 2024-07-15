from django.db import models
from django.contrib.auth.models import AbstractUser

#Choices -- break out into a separate file?
STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('in_transit', 'In Transit'),
    ('delivered', 'Delivered'),
]
ROLE_CHOICES = [
    ('courier', 'Courier'),
    ('client', 'Client'),
]

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class User(models.Model):

    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=15)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.name

#abstract user - for role based permissions in views - necessary to break out role assignment? 
#class User(AbstractUser):
#    role = models.CharField(max_length=10, choices=ROLE_CHOICES)


class Package(models.Model):

    package_id = models.AutoField(primary_key=True)
    description = models.TextField()
    weight = models.FloatField()
    dimensions = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Package {self.package_id}: {self.description}"

class Delivery(models.Model):
    delivery_id = models.AutoField(primary_key=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    courier = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courier_deliveries')
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_deliveries')
    pickup_location = models.CharField(max_length=200)
    dropoff_location = models.CharField(max_length=200)
    delivery_status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Delivery {self.delivery_id} by {self.courier.name} for {self.client.name}"
