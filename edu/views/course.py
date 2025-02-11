from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from edu.serializers import CourseSerializer
from edu.services import CourseService

class CourseListView(APIView):
    """API View to list all courses."""

    def get(self, request):
        courses = CourseService.get_all_courses()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CourseDetailView(APIView):
    """API View to retrieve a course by ID."""

    def get(self, request, id):
        course = CourseService.get_course_by_id(id)
        if course:
            serializer = CourseSerializer(course)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
