from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from rest_framework import viewsets, permissions, generics
from rest_framework.views import exception_handler
from rest_framework.response import Response
from .serializers import *
from core.models import User
from job.models import *
from core.permissions import SubscribedUser, IsOwner
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filter import *
from django.db import IntegrityError


# Create your views here.


class AllJobViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = JobRecruiter.objects.all()
    serializer_class = AllJobsSerializer
    permission_classes = [permissions.IsAuthenticated, SubscribedUser]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CategoriesFilter

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.filter(approved=True).order_by('date')
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

    def perform_create(self, serializer, *args, **kwargs):
        serializer.save(user=self.request.user)


class JobSeekerViewSet(viewsets.ModelViewSet):
    queryset = JobSeeker.objects.all()
    serializer_class = JobSeekerSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner, SubscribedUser]
    search_fields = ['applied', 'date']
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_class = ViewJobFilter

    def list(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=request.user.id)
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "User Does not exist"}, status=400)
        queryset = self.queryset.filter(user=user).order_by('-date')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):

        job = JobSeeker.objects.filter(user=self.request.user, job=self.request.data['job'], applied=True)

        # job = JobSeeker.objects.filter(user=self.request.user, job=self.request.data['job'], applied=True, saved=True)
        if job.exists():
            return Response({"error": "Already Applied"}, status=400)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer.save(user=self.request.user))
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


class ViewJobApplicationAPI(generics.RetrieveAPIView):
    queryset = JobSeeker.objects.all()
    serializer_class = ViewJobApplicationsSerializer
    permission_classes = [permissions.IsAuthenticated, SubscribedUser]
    lookup_field = ['id']

    def retrieve(self, request, *args, **kwargs):
        try:
            job = JobRecruiter.objects.get(id=self.kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "Does not exist"}, status=400)
        queryset = self.queryset.filter(job=job)
        queryset = self.filter_queryset(queryset)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=200)


class UpdateJobApplicationAPI(generics.RetrieveUpdateAPIView):
    queryset = JobSeeker.objects.all()
    serializer_class = UpdateJobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated, SubscribedUser]
    lookup_field = ['id']

    def retrieve(self, request, *args, **kwargs):
        try:
            queryset = self.queryset.get(id=self.kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "Does not exist"}, status=400)

        serializer = self.get_serializer(queryset)
        return Response(serializer.data, status=200)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.queryset.get(id=self.kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST":"Does not exist"}, status=400)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)
