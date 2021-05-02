from django.urls import path, include
from rest_framework import routers
from vendor import views


app_name = 'vendor'

router = routers.DefaultRouter()
router.register('view-vendor', views.ViewVendorViewSet, basename='viewvendor')
router.register('view-add-edit-vendor', views.VendorViewSet, basename='viewaddeditvendor')
"""router.register('view-add-business-information', views.BusinessInformationViewSet, basename='viewaddbusinessinformation')
router.register('view-add-bank-details', views.BankDetailsViewSet, basename='viewaddbankdetails')
router.register('view-add-services', views.ServicesViewSet, basename='viewaddservices')"""

urlpatterns = [
    path('', include(router.urls)),
]
