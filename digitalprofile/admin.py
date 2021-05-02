from django.contrib import admin
from django.utils.translation import ngettext
from django.contrib import messages
from .models import *

# Register your models here.


# admin.site.disable_action('delete_selected')


@admin.register(DigitalProfile)
class DigitalProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'company_name', 'date', 'approved']
    actions = ['make_approved']

    def make_approved(self, request, queryset):
        updated = queryset.update(approved=True)
        self.message_user(request, ngettext(
            '%d Profile was successfully marked as Approved.',
            '%d Profile were successfully marked as Approved.',
            updated,
        ) % updated, messages.SUCCESS)

    make_approved.short_description = "Mark Selected Profiles As Approved"


@admin.register(PersonalDetail)
class DigitalProfileAdmin(admin.ModelAdmin):
    list_display = ['digital_profile', 'name', 'mobile', 'location']


@admin.register(SocialMediaLinks)
class SocialMediaLinksAdmin(admin.ModelAdmin):
    list_display = ['digital_profile', 'user']


@admin.register(PaymentDetail)
class PaymentDetailAdmin(admin.ModelAdmin):
    list_display = ['digital_profile', 'user', 'paytm_number', 'google_pay_number', 'phonepe_number', 'account_number']


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['digital_profile', 'user', 'service_name1', 'service_name2', 'service_name3']


@admin.register(Ecommerce)
class EcommerceAdmin(admin.ModelAdmin):
    list_display = ['digital_profile', 'user', 'product_name', 'selling_price']


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['digital_profile', 'user']
