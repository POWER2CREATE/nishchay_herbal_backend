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


class DigitalProfileViewSet(viewsets.ModelViewSet):
    queryset = DigitalProfile.objects.all()
    serializer_class = DigitalProfileSerializer
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

        if DigitalProfile.objects.filter(user=request.user.id).exists():
            return Response({"ALREADY_EXIST": "Digital Profile Already Exists"}, status=400)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer.save(user=request.user))
            return Response(serializer.data, status=200)


class EditDigitalProfileViewSet(viewsets.ModelViewSet):
    queryset = DigitalProfile.objects.all()
    serializer_class = EditDigitalProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner, SubscribedUser]


class PersonalDetailViewSet(viewsets.ModelViewSet):
    queryset = PersonalDetail.objects.all()
    serializer_class = PersonalDetailSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner, SubscribedUser]

    def list(self, request, *args, **kwargs):
        try:
            digital_profile = DigitalProfile.objects.get(user=request.user.id)
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "Digital Profile Does not exist"}, status=400)
        queryset = self.queryset.filter(digital_profile=digital_profile)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        try:
            digital_profile = DigitalProfile.objects.get(user=request.user.id)
        except ObjectDoesNotExist:
            return Response({"ERROR": "Digital Profile Does not exist"}, status=400)

        if self.queryset.filter(digital_profile=digital_profile, user=request.user.id).exists():
            return Response({"error": "Already Filled Details"}, status=400)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer.save(digital_profile=digital_profile, user=request.user))
            return Response(serializer.data, status=200)


class SocialMediaLinksViewSet(viewsets.ModelViewSet):
    queryset = SocialMediaLinks.objects.all()
    serializer_class = SocialMediaLinksSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner, SubscribedUser]

    def list(self, request, *args, **kwargs):
        try:
            digital_profile = DigitalProfile.objects.get(user=request.user.id)
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "Digital Profile Does not exist"}, status=400)
        queryset = self.queryset.filter(digital_profile=digital_profile)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        try:
            digital_profile = DigitalProfile.objects.get(user=request.user.id)
        except ObjectDoesNotExist:
            return Response({"ERROR": "Digital Profile Does not exist"}, status=400)

        if self.queryset.filter(digital_profile=digital_profile, user=request.user.id).exists():
            return Response({"error": "Already Filled Details"}, status=400)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer.save(digital_profile=digital_profile, user=request.user))
            return Response(serializer.data, status=200)


class PaymentDetailViewSet(viewsets.ModelViewSet):
    queryset = PaymentDetail.objects.all()
    serializer_class = PaymentDetailSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner, SubscribedUser]

    def list(self, request, *args, **kwargs):
        try:
            digital_profile = DigitalProfile.objects.get(user=request.user.id)
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "Digital Profile Does not exist"}, status=400)
        queryset = self.queryset.filter(digital_profile=digital_profile)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        try:
            digital_profile = DigitalProfile.objects.get(user=request.user.id)
        except ObjectDoesNotExist:
            return Response({"ERROR": "Digital Profile Does not exist"}, status=400)

        if self.queryset.filter(digital_profile=digital_profile, user=request.user.id).exists():
            return Response({"error": "Already Filled Details"}, status=400)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer.save(digital_profile=digital_profile, user=request.user))
            return Response(serializer.data, status=200)


class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner, SubscribedUser]

    def list(self, request, *args, **kwargs):
        try:
            digital_profile = DigitalProfile.objects.get(user=request.user.id)
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "Digital Profile Does not exist"}, status=400)
        queryset = self.queryset.filter(digital_profile=digital_profile)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        try:
            digital_profile = DigitalProfile.objects.get(user=request.user.id)
        except ObjectDoesNotExist:
            return Response({"ERROR": "Digital Profile Does not exist"}, status=400)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer.save(digital_profile=digital_profile, user=request.user))
        return Response(serializer.data, status=200)


class EcommerceViewSet(viewsets.ModelViewSet):
    queryset = Ecommerce.objects.all()
    serializer_class = EcommerceSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner, SubscribedUser]

    def list(self, request, *args, **kwargs):
        try:
            digital_profile = DigitalProfile.objects.get(user=request.user.id)
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "Digital Profile Does not exist"}, status=400)
        queryset = self.queryset.filter(digital_profile=digital_profile)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        try:
            digital_profile = DigitalProfile.objects.get(user=request.user.id)
        except ObjectDoesNotExist:
            return Response({"ERROR": "Digital Profile Does not exist"}, status=400)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer.save(digital_profile=digital_profile, user=request.user))
        return Response(serializer.data, status=200)


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner, SubscribedUser]

    def list(self, request, *args, **kwargs):
        try:
            digital_profile = DigitalProfile.objects.get(user=request.user.id)
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "Digital Profile Does not exist"}, status=400)
        queryset = self.queryset.filter(digital_profile=digital_profile)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        try:
            digital_profile = DigitalProfile.objects.get(user=request.user.id)
        except ObjectDoesNotExist:
            return Response({"ERROR": "Digital Profile Does not exist"}, status=400)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer.save(digital_profile=digital_profile, user=request.user))
        return Response(serializer.data, status=200)


class ApproveDigitalProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DigitalProfile.objects.all()
    serializer_class = ApproveDigitalProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.filter(approved=False)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ApproveDigitalProfileDetailViewSet(viewsets.ModelViewSet):
    queryset = DigitalProfile.objects.all()
    serializer_class = ApproveDigitalProfileDetailSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]


class MyDigitalProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DigitalProfile.objects.all()
    serializer_class = MyDigitalProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def list(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=request.user.id)
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "User Does not exist"}, status=400)

        try:
            digital_profile = DigitalProfile.objects.get(user=request.user.id)
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "Digital Profile Does not exist"}, status=400)
        if DigitalProfile.objects.filter(user=request.user.id, approved=True).exists():
            queryset = self.queryset.filter(user=user)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({"DOES_NOT_APPROVED": "Currently Your Digital Profile Does not Approved By Admin"}, status=400)
