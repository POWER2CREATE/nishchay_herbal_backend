from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import *
from .models import *
from core.models import User
from core.permissions import *
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.http import Http404
from rest_framework.views import APIView
from digitalprofile import models as digipromodel


# Create your views here.


class DigitalDiaryViewSet(viewsets.ModelViewSet):
    queryset = DigitalDiary.objects.all()
    serializer_class = DigitalDiarySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner, SubscribedUser]

    def list(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=request.user.id)
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "User Does not exist"}, status=400)

        queryset = self.queryset.filter(user=user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer.save())
        return Response(serializer.data, status=200)


class DigitalGreetingCardViewSet(viewsets.ModelViewSet):
    queryset = DigitalGreetingCard.objects.all()
    serializer_class = DigitalGreetingCardSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner, SubscribedUser]

    def list(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=request.user.id)
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "User Does not exist"}, status=400)

        queryset = self.queryset.filter(user=user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save()


class DigitalVisitingCardViewSet(viewsets.ModelViewSet):
    queryset = DigitalVisitingCard.objects.all()
    serializer_class = DigitalVisitingCardSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner, SubscribedUser]

    def list(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=request.user.id)
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "User Does not exist"}, status=400)

        queryset = self.queryset.filter(user=user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save()


class AllUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AllUserSerializer

import datetime
class LeftTimeDigitalDiary(APIView):
    queryset = DigitalDiary.objects.all()
    serializer_class = LeftTimeSerializers
    permission_classes = [permissions.IsAuthenticated,]

    def get_object(self, pk):
        try:
            return DigitalDiary.objects.get(id=pk)
        except DigitalDiary.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        queryset = self.get_object(pk)

        serializer = self.serializer_class(queryset)
        return Response(serializer.data)

class VisitingCardAPI(APIView):
    serializers = VisitingSerializers
    permission_classes = [permissions.IsAuthenticated,]

    def get_object(self, pk):
        try:
            return digipromodel.DigitalProfile.objects.get(user=pk)
        except digipromodel.DigitalProfile.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        ins = self.get_object(request.user)
        queryset = DigitalVisitingCard.objects.get(user=request.user)
        serializer = self.serializer_class(queryset)
        return Response(serializer)


