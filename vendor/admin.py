from django.contrib import admin
from django.utils.translation import ngettext
from django.contrib import messages
from .models import *

# Register your models here.


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'email', 'category', 'is_active']
    """actions = ['make_approved']

    def make_approved(self, request, queryset):
        updated = queryset.update(approved=True)
        self.message_user(request, ngettext(
            '%d Profile was successfully marked as Approved.',
            '%d Profile were successfully marked as Approved.',
            updated,
        ) % updated, messages.SUCCESS)

    make_approved.short_description = "Mark Selected Profiles As Approved"""""

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(VendorServicesName)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
