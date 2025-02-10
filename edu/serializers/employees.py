from rest_framework import serializers
from edu.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ("id", "full_name", "phone", "role" )
