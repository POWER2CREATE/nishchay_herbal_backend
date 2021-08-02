from django.urls import path, include
from digitalfacilities.views import *
from rest_framework import routers


app_name = 'digitalfacilities'

router = routers.DefaultRouter()
router.register('view-add-edit-digital-diary', DigitalDiaryViewSet, basename='viewadddeditdigitaldiary')
router.register('view-add-edit-digital-greeting-card', DigitalGreetingCardViewSet, basename='viewadddeditdigitalgreetingcard')
router.register('view-add-edit-digital-visiting-card', DigitalVisitingCardViewSet, basename='viewadddeditdigitalvisitingcard')
router.register('my-users', AllUserViewSet, basename='myuser')

urlpatterns = [
    path('', include(router.urls)),
    path('time-left/<int:pk>/', LeftTimeDigitalDiary.as_view(), name='timeleftview'),
    path('digital-profile-visiting/', VisitingCardAPI.as_view(), name='visitingView'),
]
