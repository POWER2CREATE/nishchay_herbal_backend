from django.contrib import admin
from django.utils.translation import ngettext
from django.contrib import messages
from .models import *

# Register your models here.


@admin.register(JobRecruiter)
class JobAdmin(admin.ModelAdmin):
    list_display = ['id', 'job_title', 'company_name', 'your_name', 'approved', 'date']
    actions = ['make_approved']

    def make_approved(self, request, queryset):
        updated = queryset.update(approved=True)
        self.message_user(request, ngettext(
            '%d Profile was successfully marked as Approved.',
            '%d Profile were successfully marked as Approved.',
            updated,
        ) % updated, messages.SUCCESS)

    make_approved.short_description = "Mark Selected Profiles As Approved"

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(JobSeeker)
class UserJob(admin.ModelAdmin):
    list_display = ['id', 'user', 'job', 'date', 'saved', 'applied']
