from rest_framework import serializers
from .models import *


class DigitalDiarySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    user = serializers.ReadOnlyField(source='user.username')
    url = serializers.HyperlinkedIdentityField(view_name="digitalfacilities:viewadddeditdigitaldiary-detail")  # CALL JOB DETAIL ROUTER
    days_left = serializers.ReadOnlyField()

    class Meta:
        model = DigitalDiary
        fields = '__all__'


class DigitalGreetingCardSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    user = serializers.ReadOnlyField(source='user.username')
    url = serializers.HyperlinkedIdentityField(view_name="digitalfacilities:viewadddeditdigitalgreetingcard-detail")  # CALL JOB DETAIL ROUTER

    class Meta:
        model = DigitalGreetingCard
        fields = '__all__'


class DigitalVisitingCardSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    user = serializers.ReadOnlyField(source='user.username')
    url = serializers.HyperlinkedIdentityField(view_name="digitalfacilities:viewadddeditdigitalvisitingcard-detail")  # CALL JOB DETAIL ROUTER

    class Meta:
        model = DigitalVisitingCard
        fields = '__all__'
