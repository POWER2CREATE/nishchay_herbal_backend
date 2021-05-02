from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    user = serializers.ReadOnlyField(source='user.username')
    url = serializers.HyperlinkedIdentityField(view_name='ecommerce:viewadddeditproduct-detail')

    class Meta:
        model = Product
        fields = '__all__'


class RatingReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = RatingReview
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Cart
        fields = '__all__'
