from django.urls import path
from recruit.views import MatchJobSkillsView


urlpatterns = [
    # Your other URL patterns here
    path('validate-resume/', MatchJobSkillsView.as_view(), name='validate_resume'),
]
