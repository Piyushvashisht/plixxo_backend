from rest_framework import serializers
from Reevaluation.models import Reevaluation

class ReevaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reevaluation
        fields = '__all__'
        