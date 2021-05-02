from rest_framework import serializers
from .models import *
from core.models import User


class AllJobsSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    user = serializers.ReadOnlyField(source='user.username')
    url = serializers.HyperlinkedIdentityField(view_name="job:viewalljob-detail")  # CALL JOB DETAIL ROUTER

    class Meta:
        model = JobRecruiter
        # fields = ['url', 'id', 'user', 'job_title', 'company_name', 'location', 'salary_from', 'salary_to', 'date']
        fields = '__all__'


class JobDetailSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    user = serializers.ReadOnlyField(source='user.username')
    company_name = serializers.ReadOnlyField()
    job_title = serializers.ReadOnlyField()
    location = serializers.ReadOnlyField()
    your_name = serializers.ReadOnlyField()
    phone = serializers.ReadOnlyField()
    industry = serializers.ReadOnlyField()
    experience = serializers.ReadOnlyField()
    salary_from = serializers.ReadOnlyField()
    salary_to = serializers.ReadOnlyField()
    approved = serializers.ReadOnlyField()

    class Meta:
        model = JobRecruiter
        fields = '__all__'


class JobRecruiterSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    user = serializers.ReadOnlyField(source='user.username')
    url = serializers.HyperlinkedIdentityField(view_name="job:editviewjobdetail-detail")  # CALL JOB DETAIL ROUTER
    active = serializers.ReadOnlyField()
    approved = serializers.ReadOnlyField()

    class Meta:
        model = JobRecruiter
        fields = ['url', 'id', 'user', 'company_name', 'job_title', 'location', 'your_name', 'phone', 'industry', 'experience', 'salary_from', 'salary_to', 'date', 'approved', 'description', 'requirements', 'active']


class AppliedJobMiniDetailSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    url = serializers.HyperlinkedIdentityField(view_name="job:editviewjobdetail-detail")  # CALL VIEW APPLY JOB ROUTER

    class Meta:
        model = JobRecruiter
        fields = ['url', 'id', 'job_title', 'company_name', 'location']


class JobSeekerSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    user = serializers.ReadOnlyField(source='user.username')
    # url = serializers.HyperlinkedIdentityField(view_name="job:editviewjobdetail-detail")  # CALL VIEW APPLY JOB ROUTER
    # job = serializers.HyperlinkedRelatedField(queryset=JobRecruiter.objects.all(), view_name="job:editviewjobdetail-detail")  # PRINT URL OF USER APPLIED JOB DETAIL THROUGH VIEW ADD JOB ROUTER

    class Meta:
        model = JobSeeker
        fields = ['id', 'job', 'user', 'resume', 'date', 'saved', 'applied']


class UserAppliedJobSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    # url = serializers.HyperlinkedIdentityField(view_name="job:editviewjobdetail-detail")  # CALL VIEW APPLY JOB ROUTER
    user = serializers.ReadOnlyField(source='user.username')
    job = AppliedJobMiniDetailSerializer()

    class Meta:
        model = JobSeeker
        fields = ['id', 'job', 'date', 'status', 'user']


class UserSavedJobSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    url = serializers.HyperlinkedIdentityField(view_name="job:viewalljob-detail")  # CALL VIEW APPLY JOB ROUTER
    user = serializers.ReadOnlyField(source='user.username')
    job = AppliedJobMiniDetailSerializer()

    class Meta:
        model = JobSeeker
        fields = ['url', 'id', 'job', 'date', 'status', 'user']


class AllJobApplicationsSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = JobSeeker
        fields = '__all__'


class ViewHireUserSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    url = serializers.HyperlinkedIdentityField(view_name="job:viewalljobapplications-detail")  # CALL JOB DETAIL ROUTER
    active = serializers.ReadOnlyField()
    approved = serializers.ReadOnlyField()

    class Meta:
        model = JobRecruiter
        fields = '__all__'


class ViewJobApplicationsSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.name')

    class Meta:
        model = JobSeeker
        fields = '__all__'


class UpdateJobApplicationSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    user = serializers.ReadOnlyField(source='user.name')

    class Meta:
        model = JobSeeker
        fields = ['id', 'user', 'status', 'date']
