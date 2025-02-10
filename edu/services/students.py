from django.db.models import QuerySet
from edu.models import Student

class StudentService:
    @staticmethod
    def get_all_students() -> QuerySet:
        """Returns all students."""
        return Student.objects.all()


    @staticmethod
    def get_student_by_id(student_id: int) -> Student | None:
        """Returns a student by ID or None if not found."""
        return Student.objects.filter(id=student_id).first()


