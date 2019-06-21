from rest_framework import serializers
from Campaign_content.models import Campaign_content

class Campaign_contentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign_content
        fields = '__all__'
        