from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from edu.serializers import StudentSerializer, UpdateBalanceSerializer
from edu.services import StudentService

class StudentListView(APIView):
    """View to list all students using StudentService."""

    def get(self, request):
        students = StudentService.get_all_students()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StudentDetailView(APIView):
    """View to retrieve a student by ID using StudentService."""

    def get(self, request, id):
        student = StudentService.get_student_by_id(id)
        if student:
            serializer = StudentSerializer(student)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "Student not found"}, status=status.HTTP_404_NOT_FOUND)


class UpdateBalanceView(APIView):
    """View to update a student's balance."""

    def post(self, request, id):
        serializer = UpdateBalanceSerializer(data=request.data)
        if serializer.is_valid():
            try:
                student = StudentService.update_student_balance(id, serializer.validated_data["amount"])
                return Response({"message": "Balance updated successfully", "new_balance": student.balance},
                                status=status.HTTP_200_OK)
            except ValidationError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)