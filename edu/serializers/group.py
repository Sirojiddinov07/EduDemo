from rest_framework import serializers
from edu.models import Group


class GroupSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source="course.title", read_only=True)
    instructor_name = serializers.CharField(source="instructor.full_name", read_only=True)
    student_count = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ("id", "name", "course", "course_title",
                  "instructor", "instructor_name", "students", "student_count")

    def get_student_count(self, obj):
        return obj.students.count()
