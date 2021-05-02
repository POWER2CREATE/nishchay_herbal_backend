from django.contrib import admin
from digitalfacilities.models import *


# Register your models here.

@admin.register(DigitalDiary)
class DigitalDiaryAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'start_date', 'days_left', 'reminder', 'date']


@admin.register(DigitalGreetingCard)
class DigitalGreetingCardAdmin(admin.ModelAdmin):
    list_display = ['user', 'sender', 'receiver', 'category', 'date']


@admin.register(DigitalVisitingCard)
class DigitalVisitingCardAdmin(admin.ModelAdmin):
    list_display = ['user', 'business_name', 'email', 'category', 'date']
