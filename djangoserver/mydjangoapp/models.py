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
# a generic Post, to be filled out later for orders 
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)  # Pseudonym
    contact = models.CharField(max_length=32)  # phone or instant message id?
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    pubk = models.CharField(max_length=4096)  # pub key; for now, Check Diffie Helman v14 encryption later
    prik = models.CharField(max_length=4096)  # private key; for now, Check Diffie Helman v14 encryption later
    pymnt = models.CharField(max_length=32)  # maybe a hashed dict where the info is scrambled but retrievable?
    vehicle = models.CharField(max_length=80, null=True)

    def __str__(self):
        return self.name

#abstract user - for role based permissions in views - necessary to break out role assignment? 
#class User(AbstractUser):
#    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

#marketplace..... these are the packages built to deliver. 
class Package(models.Model):
    # created by the vendor (origin) and put on sale
    package_id = models.AutoField(primary_key=True)
    description = models.TextField()
    weight = models.FloatField()
    dimensions = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='packages')
    courier = models.CharField(max_length=100)  # unsure about this one. when deliver is ordered, package gets a courier associated

    def __str__(self):
        return f"Package {self.package_id}: {self.description}"

class Delivery(models.Model):
    # this is the "order" - created by customer after selecting a package
    delivery_id = models.AutoField(primary_key=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    courier = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courier_deliveries')
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_deliveries')
    pickup_location = models.CharField(max_length=200)
    dropoff_location = models.CharField(max_length=200)
    delivery_status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Delivery {self.delivery_id} by {self.courier.name} for {self.client.name}"

#transaction or audit database - this is where one of the anon features must be; 

