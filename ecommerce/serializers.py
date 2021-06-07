from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    user = serializers.ReadOnlyField(source='user.email')
    url = serializers.HyperlinkedIdentityField(view_name='ecommerce:viewadddeditproduct-detail')

    class Meta:
        model = Product
        fields = '__all__'


class CartProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = ['product_name', 'product_image1', 'product_mrp', 'selling_price', 'category']


class RatingReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = RatingReview
        fields = '__all__'


class AddToCartSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    user = serializers.ReadOnlyField(source='user.email')
    url = serializers.HyperlinkedIdentityField(view_name='ecommerce:viewaddcart-detail')
    # product = serializers.HyperlinkedIdentityField(view_name='ecommerce:viewallproduct-detail')
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = Cart
        fields = '__all__'


class ViewMyCartSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    url = serializers.HyperlinkedIdentityField(view_name='ecommerce:editcart-detail')
    product = CartProductSerializer()

    class Meta:
        model = Cart
        fields = '__all__'


class EditCartSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    product = CartProductSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'
