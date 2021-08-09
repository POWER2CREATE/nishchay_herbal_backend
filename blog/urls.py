from django.urls import path, include
from .views import *
from rest_framework import routers


app_name = 'blog'

urlpatterns = [
    path('bloglistandcreate/', PostCreateAndListView.as_view({'get': 'list'}), name='bloglistandcreate'),
    path('blogdeleteUpdate/<int:pk>/', BlogDelUpdate.as_view(), name='blogdeleteview'),
]