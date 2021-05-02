from django.shortcuts import render
from . import models, serializers
from rest_framework import viewsets, status, permissions, generics
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import *
from rest_framework.response import Response

# Create your views here.


class UserSerializerAPIViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated,]
    http_method_names = ['post', 'head','options']

    def get_permissions(self):
        if self.action == 'post':
            permission_classes = [IsAuthenticated]
            # user = self.queryset.get(id=self.request.user.id)
            # if user.isadmin:
            #     permission_classes = [IsAuthenticated]
            # else:
            #     return Response("error",status=401)
        else:
            permission_classes = [IsAdminUser]
            # permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class UserProfileUpdateView(generics.RetrieveUpdateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserProfileUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = ['id']

    def retrieve(self, request, *args, **kwargs):
        try:
            queryset = self.queryset.get(id=request.user.id)
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "Does not exist"}, status=400)

        serializer = self.get_serializer(queryset)
        return Response(serializer.data, status=200)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.queryset.get(id=request.user.id)
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST":"Does not exist"}, status=400)
        if request.user.is_customer:
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response({"USER_ERROR":"User is not customer"}, status=400)
