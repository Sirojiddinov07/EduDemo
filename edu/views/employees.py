from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from edu.serializers import EmployeeSerializer
from edu.services import EmployeeService

class EmployeeListView(APIView):
    """API View to list all employees."""

    def get(self, request):
        employees = EmployeeService.get_all_employees()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EmployeeDetailView(APIView):
    """API View to retrieve an employee by ID."""

    def get(self, request, id):
        employee = EmployeeService.get_employee_by_id(id)
        if employee:
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
