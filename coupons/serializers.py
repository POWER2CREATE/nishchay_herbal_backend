from rest_framework import serializers
from .models import *
from core.models import User
import datetime

class RewardSerializer(serializers.ModelSerializer):

    class Meta:
        model = RewardSystem
        fields ='__all__'

class RewardCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = RewardCode
        fields = "__all__"

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        # fields = '__all__'
        exclude = ('user', )