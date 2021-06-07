from django.contrib import admin
from . models import *

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'fullname', 'email', 'mobile', 'is_customer', 'is_superuser', 'subscribed']
    list_filter = ['subscribed']

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True


@admin.register(SubscriptionPlans)
class SubscriptionPlansAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'months', 'price', 'active']
    list_filter = ['months', 'active']

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True


@admin.register(UserSubscription)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'subscription_plan', 'active', 'date']
    list_filter = ['active', 'date']

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True
