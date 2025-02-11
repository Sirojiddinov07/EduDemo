from rest_framework import serializers
from edu.models import Student

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ("id", "full_name", "phone", "balance", "status" )

from rest_framework import serializers

class UpdateBalanceSerializer(serializers.Serializer):
    amount = serializers.IntegerField()

    def validate_amount(self, value):
        if value == 0:
            raise serializers.ValidationError("Amount cannot be zero.")
        return value

