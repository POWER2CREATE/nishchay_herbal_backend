from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=12, null=True)
    address = models.TextField(max_length=200, null=True, blank=True)
    pincode = models.IntegerField(null=True, blank=True)
    occupation = models.CharField(max_length=12, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    notification_token = models.CharField(max_length=64, blank=True, null=True)
    passwordchanged = models.BooleanField(default=False)
    subscribed = models.BooleanField(default=True)
