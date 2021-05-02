from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from .serializers import *
from .models import *
from core.models import User
from core.permissions import *
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def list(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=request.user.id)
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "User Does not exist"}, status=400)

        queryset = self.queryset.filter(user=user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):

        if request.user.is_customer is False:
            return Response({"error": "You are not Customer"}, status=400)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer.save(user=request.user))
        return Response(serializer.data, status=200)


class ViewVendorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [permissions.IsAuthenticated]


"""class BusinessInformationViewSet(viewsets.ModelViewSet):
    queryset = BusinessInformation.objects.all()
    serializer_class = BusinessInformationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        try:
            vendor = Vendor.objects.get(user=request.user)
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "Does not exist"}, status=400)
        queryset = self.queryset.filter(job=job)
        queryset = self.filter_queryset(queryset)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def create(self, request, *args, **kwargs):
        if request.user.is_customer is False:
            return Response({"error": "You are not User"}, status=400)
        try:
            vendor = Vendor.objects.get(user=request.user)
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "Does not exist"}, status=400)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer.save(user=request.user, vendor=vendor))
        return Response(serializer.data, status=200)


class BankDetailsViewSet(viewsets.ModelViewSet):
    queryset = BankDetails.objects.all()
    serializer_class = BankDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if request.user.is_customer is False:
            return Response({"error": "You are not User"}, status=400)
        try:
            vendor = Vendor.objects.get(user=request.user)
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "Does not exist"}, status=400)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer.save(user=request.user, vendor=vendor))
        return Response(serializer.data, status=200)


class ServicesViewSet(viewsets.ModelViewSet):
    queryset = VendorServices.objects.all()
    serializer_class = VendorServicesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if request.user.is_customer is False:
            return Response({"error": "You are not User"}, status=400)
        try:
            vendor = Vendor.objects.get(user=request.user)
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "Does not exist"}, status=400)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer.save(user=request.user, vendor=vendor))
        return Response(serializer.data, status=200)"""
