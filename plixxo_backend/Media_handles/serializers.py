from rest_framework import serializers
from Media_handles.models import Media_handles

class Media_handlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media_handles
        fields = '__all__'
        