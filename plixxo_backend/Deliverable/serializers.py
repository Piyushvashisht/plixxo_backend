from rest_framework import serializers
from Deliverable.models import Deliverable

class DeliverableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliverable
        fields = '__all__'
        