from django.urls import path
from recruit.resumeExtract.resume_views import ResumeAPIView
from recruit.views import MatchJobSkillsView

urlpatterns = [
    # Your other URL patterns here
    path('resume-parse/', ResumeAPIView.as_view(), name='resume-parse'),
    path('validate-resume/', MatchJobSkillsView.as_view(), name='validate-resume'),
]