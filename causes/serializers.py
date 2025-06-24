from rest_framework import serializers
from .models import *

class CauseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cause
        fields = '__all__'


class ContributionSerializer(serializers.ModelSerializer):
    cause = CauseSerializer(read_only=True)
    class Meta:
        model = Contribution
        fields = '__all__'
        read_only_fields = ['cause']

    def create(self, validated_data):
        cause_id = self.context.get('cause_id')

        try:
            cause = Cause.objects.get(id=cause_id)
        except Cause.DoesNotExist:
            raise serializers.ValidationError("Invalid cause ID in URL.")
        
        validated_data["cause"] = cause
        return Contribution.objects.create(**validated_data)

    def validate_amount(self, amount):
        if amount <= 0:
            raise serializers.ValidationError("Contribution amount must be greater than 0.")
        
        return amount