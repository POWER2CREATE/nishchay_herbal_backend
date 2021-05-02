from django.urls import path, include
from digitalprofile.views import *
from rest_framework import routers


app_name = 'digitalprofile'

router = routers.DefaultRouter()
router.register('view-my-digital-profile', MyDigitalProfileViewSet, basename='viewmydigitalprofile')
router.register('view-add-digital-profile', DigitalProfileViewSet, basename='viewadddigitalprofile')
router.register('edit-digital-profile', EditDigitalProfileViewSet, basename='editdigitalprofile')
router.register('view-add-edit-personal-detail', PersonalDetailViewSet, basename='viewaddeditpersonaldetail')
router.register('view-add-edit-social-media-links', SocialMediaLinksViewSet, basename='viewaddeditsocialmedialinks')
router.register('view-add-edit-payment-detail', PaymentDetailViewSet, basename='viewaddeditpaymentdetail')
router.register('view-add-edit-services', ServicesViewSet, basename='viewaddeditservices')
router.register('view-add-edit-ecommerce', EcommerceViewSet, basename='viewaddeditecommerce')
router.register('view-add-edit-gallery', GalleryViewSet, basename='viewaddeditgallery')
router.register('approved-digital-profile', ApproveDigitalProfileViewSet, basename='approvedigitalprofile')
router.register('approved-digital-profile-detail', ApproveDigitalProfileDetailViewSet, basename='approvedigitalprofiledetail')

urlpatterns = [
    path('', include(router.urls)),
]
