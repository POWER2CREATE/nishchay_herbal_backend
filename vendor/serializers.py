from rest_framework import serializers
from .models import *


class VendorSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    user = serializers.ReadOnlyField(source='user.username')
    url = serializers.HyperlinkedIdentityField(view_name='vendor:viewaddeditvendor-detail')

    class Meta:
        model = Vendor
        fields = '__all__'


"""class BusinessInformationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    # url = serializers.HyperlinkedIdentityField(view_name='ecommerce:viewadddeditproduct-detail')

    class Meta:
        model = BusinessInformation
        fields = '__all__'


class BankDetailsSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    # url = serializers.HyperlinkedIdentityField(view_name='ecommerce:viewadddeditproduct-detail')

    class Meta:
        model = BankDetails
        fields = '__all__'


class VendorServicesSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    # url = serializers.HyperlinkedIdentityField(view_name='ecommerce:viewadddeditproduct-detail')

    class Meta:
        model = VendorServices
        fields = '__all__'"""
