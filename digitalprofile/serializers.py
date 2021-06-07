from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from .models import *
from core.models import User


class DigitalProfileSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="digitalprofile:editdigitalprofile-detail")  # CALL JOB DETAIL ROUTER
    user = serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = DigitalProfile
        fields = ['id', 'user', 'company_name', 'company_logo']


class DigitalProfileMiniSerializer(serializers.ModelSerializer):

    class Meta:
         model = DigitalProfile
         fields = ['id']


class EditDigitalProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    company_name = serializers.ReadOnlyField()
    approved = serializers.ReadOnlyField()

    class Meta:
        model = DigitalProfile
        fields = '__all__'


class PersonalDetailSerializer(serializers.ModelSerializer):
    digital_profile = DigitalProfileMiniSerializer(read_only=True)
    user = serializers.ReadOnlyField(source='user.email')
    # url = serializers.HyperlinkedIdentityField(view_name="digitalprofile:viewaddeditpersonaldetail-detail")

    class Meta:
        model = PersonalDetail
        fields = '__all__'


class SocialMediaLinksSerializer(serializers.HyperlinkedModelSerializer):
    digital_profile = DigitalProfileMiniSerializer(read_only=True)
    user = serializers.ReadOnlyField(source='user.email')
    url = serializers.HyperlinkedIdentityField(view_name="digitalprofile:viewaddeditsocialmedialinks-detail")

    class Meta:
        model = SocialMediaLinks
        fields = '__all__'


class PaymentDetailSerializer(serializers.HyperlinkedModelSerializer):
    digital_profile = DigitalProfileMiniSerializer(read_only=True)
    user = serializers.ReadOnlyField(source='user.email')
    url = serializers.HyperlinkedIdentityField(view_name="digitalprofile:viewaddeditpaymentdetail-detail")

    class Meta:
        model = PaymentDetail
        fields = '__all__'


class ServicesSerializer(serializers.HyperlinkedModelSerializer):
    digital_profile = DigitalProfileMiniSerializer(read_only=True)
    user = serializers.ReadOnlyField(source='user.email')
    url = serializers.HyperlinkedIdentityField(view_name="digitalprofile:viewaddeditservices-detail")

    class Meta:
        model = Services
        fields = '__all__'


class EcommerceSerializer(serializers.HyperlinkedModelSerializer):
    digital_profile = DigitalProfileMiniSerializer(read_only=True)
    user = serializers.ReadOnlyField(source='user.email')
    url = serializers.HyperlinkedIdentityField(view_name="digitalprofile:viewaddeditecommerce-detail")

    class Meta:
        model = Ecommerce
        fields = '__all__'


class GallerySerializer(serializers.HyperlinkedModelSerializer):
    digital_profile = DigitalProfileMiniSerializer(read_only=True)
    user = serializers.ReadOnlyField(source='user.email')
    url = serializers.HyperlinkedIdentityField(view_name="digitalprofile:viewaddeditgallery-detail")

    class Meta:
        model = Gallery
        fields = '__all__'


class ApproveDigitalProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    url = serializers.HyperlinkedIdentityField(view_name="digitalprofile:approvedigitalprofiledetail-detail")
    company_name = serializers.ReadOnlyField()

    class Meta:
        model = DigitalProfile
        fields = '__all__'


class ApproveDigitalProfileDetailSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    company_name = serializers.ReadOnlyField()

    class Meta:
        model = DigitalProfile
        fields = ['user', 'company_name', 'date', 'approved']


class PersonalDetailMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalDetail
        exclude = ['user', 'digital_profile', 'id']


class SocialMediaLinksMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaLinks
        exclude = ['user', 'digital_profile', 'id']


class PaymentDetailMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetail
        exclude = ['user', 'digital_profile', 'id']


class ServicesMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        exclude = ['user', 'digital_profile', 'id']


class EcommerceMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ecommerce
        exclude = ['user', 'digital_profile', 'id']


class GalleryMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        exclude = ['user', 'digital_profile', 'id']


class MyDigitalProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    personalDetails = serializers.SerializerMethodField(read_only=True)
    socialMediaLinks = serializers.SerializerMethodField(read_only=True)
    paymentDetails = serializers.SerializerMethodField(read_only=True)
    service = serializers.SerializerMethodField(read_only=True)
    ecommerce = serializers.SerializerMethodField(read_only=True)
    gallery = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = DigitalProfile
        fields = '__all__'

    def get_personalDetails(self, obj):
        try:
            detail = PersonalDetail.objects.get(user=obj.user.id)
        except ObjectDoesNotExist:
            return 'Please Add Personal Details'
        serializer = PersonalDetailMiniSerializer(detail)
        return serializer.data

    def get_socialMediaLinks(self, obj):
        try:
            detail = SocialMediaLinks.objects.get(user=obj.user.id)
        except ObjectDoesNotExist:
            return 'Please Add Social Media Links'
        serializer = SocialMediaLinksMiniSerializer(detail)
        return serializer.data

    def get_paymentDetails(self, obj):
        try:
            detail = PaymentDetail.objects.get(user=obj.user.id)
        except ObjectDoesNotExist:
            return 'Personal Add Payment Details'
        serializer = PaymentDetailMiniSerializer(detail)
        return serializer.data

    def get_service(self, obj):
        try:
            detail = Services.objects.filter(user=obj.user.id)
        except ObjectDoesNotExist:
            return 'Personal Add Services'
        serializer = ServicesMiniSerializer(detail, many=True)
        return serializer.data

    def get_ecommerce(self, obj):
        try:
            detail = Ecommerce.objects.filter(user=obj.user.id)
        except ObjectDoesNotExist:
            return 'Personal Add Ecommerce Products'
        serializer = EcommerceMiniSerializer(detail, many=True)
        return serializer.data

    def get_gallery(self, obj):
        try:
            detail = Gallery.objects.filter(user=obj.user.id)
        except ObjectDoesNotExist:
            return 'Personal Add Images in Gallery'
        serializer = GalleryMiniSerializer(detail, many=True)
        return serializer.data
