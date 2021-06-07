from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from .serializers import *
from core.models import User
from job.models import *
from core.permissions import SubscribedUser, IsOwner
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filter import *


# Create your views here.


class AllJobViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = JobRecruiter.objects.all()
    serializer_class = AllJobsSerializer
    permission_classes = [permissions.IsAuthenticated, SubscribedUser]
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_class = CategoriesFilter

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.filter(approved=True, active=True).order_by('date')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class JobDetailedViewSet(viewsets.ModelViewSet):
    queryset = JobRecruiter.objects.all()
    serializer_class = JobDetailSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner, SubscribedUser]


class JobRecruiterViewSet(viewsets.ModelViewSet):
    queryset = JobRecruiter.objects.all()
    serializer_class = JobRecruiterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwner, SubscribedUser]

    def list(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=request.user.id)
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "User Does not exist"}, status=400)

        queryset = self.queryset.filter(user=user).order_by('-date')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class JobSeekerViewSet(viewsets.ModelViewSet):
    queryset = JobSeeker.objects.all()
    serializer_class = JobSeekerSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner, SubscribedUser]
    http_method_names = ['post', 'options', 'head']

    def create(self, request, *args, **kwargs):

        job = JobSeeker.objects.filter(user=self.request.user, job=self.request.data['job'], applied=True)

        if job.exists():
            return Response({"error": "Already Applied"}, status=400)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer.save())
            return Response({"msg": "Successfully Applied"}, status=200)


class UserAppliedJobViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = JobSeeker.objects.all()
    serializer_class = UserAppliedJobSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner, SubscribedUser]

    def list(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=request.user.id)
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "User Does not exist"}, status=400)
        queryset = self.queryset.filter(user=user, applied=True).order_by('-date')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class UserSavedJobViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = JobSeeker.objects.all()
    serializer_class = UserAppliedJobSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner, SubscribedUser]

    def list(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=request.user.id)
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "User Does not exist"}, status=400)
        queryset = self.queryset.filter(user=user, applied=False, saved=True).order_by('-date')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class AllJobApplicationsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = JobSeeker.objects.all()
    serializer_class = AllJobApplicationsSerializer
    permission_classes = [permissions.IsAuthenticated]


class ViewHireUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = JobRecruiter.objects.all()
    serializer_class = ViewHireUserSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner, SubscribedUser]

    def list(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=request.user.id)
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "User Does not exist"}, status=400)
        queryset = self.queryset.filter(user=user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ViewJobApplicationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = JobSeeker.objects.all()
    serializer_class = ViewJobApplicationsSerializer
    permission_classes = [permissions.IsAuthenticated, SubscribedUser]

    def retrieve(self, request, *args, **kwargs):
        try:
            job = JobRecruiter.objects.get(id=self.kwargs["pk"])
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "Does not exist"}, status=400)
        queryset = self.queryset.filter(job=job)
        queryset = self.filter_queryset(queryset)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=200)


class UpdateJobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobSeeker.objects.all()
    serializer_class = UpdateJobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated, SubscribedUser]
    http_method_names = ['put', 'options', 'head', 'get']

    def retrieve(self, request, *args, **kwargs):
        try:
            queryset = self.queryset.get(id=self.kwargs["pk"])
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "Does not exist"}, status=400)

        serializer = self.get_serializer(queryset)
        return Response(serializer.data, status=200)

    def partial_update(self, request, *args, **kwargs):
        try:
            instance = self.queryset.get(id=self.kwargs["pk"])
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST":"Does not exist"}, status=400)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)
