from django.urls import path, include
from rest_framework import routers
from job import views


app_name = 'job'

router = routers.DefaultRouter()
router.register('view-all-job', views.AllJobViewSet, basename='viewalljob')
router.register('view-all-job-applications', views.AllJobApplicationsViewSet, basename='viewalljobapplications')
router.register('view-post-job-user', views.JobRecruiterViewSet, basename='viewpostjobuser')  # FOR  JOB RECRUITERS
router.register('view-hire-job-applications', views.ViewHireUserViewSet, basename='viewhirejobapplications')# FOR  JOB RECRUITERS
router.register('apply-save-job', views.JobSeekerViewSet, basename='applysavejob')  # FOR  JOB SEEKERS
router.register('view-applied-job', views.UserAppliedJobViewSet, basename='viewappliedjob')  # FOR JOB SEEKERS
router.register('view-saved-job', views.UserSavedJobViewSet, basename='viewsavedjob')  # FOR JOB SEEKERS
router.register('edit-view-job-detail', views.JobDetailedViewSet, basename='editviewjobdetail')  # FOR BOTH


urlpatterns = [
    path('', include(router.urls)),
    path('job-application/<int:id>', views.ViewJobApplicationAPI.as_view(), name='jobapplication'),
    path('job-application-update/<int:id>', views.UpdateJobApplicationAPI.as_view(), name='jobapplicationupdate'),
]
