from rest_framework import serializers
from Bank_details.models import Bank_details

class Bank_detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank_details
        fields = '__all__'
        