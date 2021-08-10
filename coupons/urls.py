from django.urls import path, include
from .views import *
from rest_framework import routers


app_name = 'coupon'

urlpatterns = [
    path('coupon-list/', CouponView.as_view({'get': 'list'}), name='couponlist'),
    path('redeem-coupon/<int:pk>/', RedeemCoupon.as_view(), name='redeem-coupon'),
    path('reward-code-list/',rewardcodeList.as_view({'get': 'list'})),
    path('referal-code-points/', ReferralcodeAPI.as_view()),
]