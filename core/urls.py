from django.urls import path, include
from rest_framework import routers
from core import views


app_name = 'core'

router = routers.DefaultRouter()

router.register('my-users', views.AllUserViewSet, basename='myuser')

urlpatterns = [
	path('', include(router.urls)),
    # path('profile-update/', views.UserProfileUpdateView.as_view(), name='profileupdate'),
]
