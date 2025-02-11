from django.db.models import QuerySet
from edu.models import Course

class CourseService:
    @staticmethod
    def get_all_courses() -> QuerySet:
        """Returns all courses."""
        return Course.objects.all()

    @staticmethod
    def get_course_by_id(course_id: int) -> Course | None:
        """Returns a course by ID"""
        return Course.objects.get(id=course_id)
