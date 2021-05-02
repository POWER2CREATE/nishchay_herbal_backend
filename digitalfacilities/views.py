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
        self.perform_create(serializer.save(user=request.user))
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
        serializer.save(user=self.request.user)


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
        serializer.save(user=self.request.user)
