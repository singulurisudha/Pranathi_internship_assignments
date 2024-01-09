from rest_framework import serializers
from recruit.models import Candidate, Job

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('resume_id', 'resume')

    
    