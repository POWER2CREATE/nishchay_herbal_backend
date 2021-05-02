from django.urls import path, include
from rest_framework import routers
from core import views


app_name = 'core'

urlpatterns = [
    path('profile-update/', views.UserProfileUpdateView.as_view(), name='profileupdate'),
]
