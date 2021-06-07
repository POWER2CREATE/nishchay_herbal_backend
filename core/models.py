from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UserManager


# Create your models here.


GENDER = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(unique=True)
    fullname = models.CharField(max_length=60, null=True)
    mobile = models.CharField(max_length=13, null=True)
    address1 = models.TextField(max_length=80, null=True)
    address2 = models.TextField(max_length=80, null=True)
    state = models.TextField(max_length=30, null=True)
    country = models.CharField(max_length=40, null=True)
    pincode = models.IntegerField(null=True)
    land_mark = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=12, choices=GENDER)
    is_customer = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    notification_token = models.CharField(max_length=64, blank=True, null=True)
    passwordchanged = models.BooleanField(default=False)
    subscribed = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['first_name', 'last_name']


class SubscriptionPlans(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    months = models.IntegerField()
    price = models.IntegerField()
    active = models.BooleanField()

    def __str__(self):
        return str(self.name)


class UserSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    subscription_plan = models.ForeignKey(SubscriptionPlans, on_delete=models.PROTECT)
    active = models.BooleanField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
