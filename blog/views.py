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
from django.db.models import Q


class PostCreateAndListView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsCustomer]
    
    def get_queryset(self):
        try:
            queryset = self.queryset.filter(user=self.request.user)
        except Post.DoesNotExist:
            return Response({"DOESNT_EXIST": "No object in post list"}, status=402)
        title = self.request.query_params.get('title', None)
        # print(title)
        if title is not None:
            queryset = queryset.filter(Q(title__icontains=title))

        return queryset

    # def list(self, request, *args, **kwargs):
    #     try:
    #         # print(request.user.id)
    #         blog = User.objects.get(id=request.user.id)
    #     except ObjectDoesNotExist:
    #         return Response({"DOES_NOT_EXIST": "User Does not exist"}, status=400)
        # try:
        #     queryset = self.queryset.filter(user=request.user)
        # except Post.DoesNotExist:
        #     return Response({"DOESNT_EXIST": "No object in post list"}, status=402)
    #     serializer = self.serializer_class(queryset, many=True)
    #     return Response(serializer.data, status=200)

    def post(self, request, *args, **kwargs):
        
        if request.data['user'] is None:
            request.data['user'] = request.user
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FilterPost(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsCustomer]

    def get_queryset(self):
        queryset = self.queryset
        print(queryset)
        title = self.request.query_params.get('title', None)
        print(title)
        if title is not None:
            queryset = queryset.filter(Q(title__icontains=title))

        return queryset

class BlogDelUpdate(APIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsCustomer]

    def get_object(self, pk):
        try:
            return Post.objects.get(id=pk)
        except Post.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = self.serializer_class(snippet)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = PostSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



