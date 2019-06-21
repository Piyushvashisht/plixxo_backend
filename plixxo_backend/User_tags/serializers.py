from rest_framework import serializers
from User_tags.models import User_tags

class User_tagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_tags
        fields = '__all__'
        