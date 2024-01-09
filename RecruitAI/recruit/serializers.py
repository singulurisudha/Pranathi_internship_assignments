from rest_framework import serializers

class MatchJobSkillsSerializer(serializers.Serializer):
    
    resume = serializers.FileField(required=True)

    def validate(self, data):
        if 'resume' not in data:
            raise serializers.ValidationError("Resume is required...")
        return data
