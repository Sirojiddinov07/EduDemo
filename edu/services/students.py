from django.core.exceptions import ValidationError
from django.db import transaction
from edu.models import Student


class StudentService:
    @staticmethod
    def get_all_students():
        """Returns all students."""
        return Student.objects.all()

    @staticmethod
    def get_student_by_id(student_id: int):
        """Returns a student by ID or None if not found."""
        return Student.objects.filter(id=student_id).first()

    @staticmethod
    def update_student_balance(student_id: int, amount: int):
        """Updates the student's balance by adding the given amount."""
        student = StudentService.get_student_by_id(student_id)
        if not student:
            raise ValidationError("Student not found")

        if amount <= 0:
            raise ValidationError("Amount cannot be zero")

        with transaction.atomic():
            student.balance += amount
            student.save()

        return student
