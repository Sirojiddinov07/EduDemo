from django.db import models
from edu.models import AbstractModel

class Group(AbstractModel):
    name = models.CharField(max_length=100, unique=True)
    course = models.ForeignKey("Course", on_delete=models.CASCADE, related_name="groups")
    instructor = models.ForeignKey("Employee", on_delete=models.SET_NULL, null=True, blank=True, related_name="groups")
    students = models.ManyToManyField("Student", related_name="groups", blank=True)

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    def __str__(self):
        return f"{self.name} - {self.course.title}"

    def add_student(self, student):
        """Adds a student to the group."""
        self.students.add(student)

    def remove_student(self, student):
        """Removes a student from the group."""
        self.students.remove(student)

    def student_count(self):
        """Returns the number of students in the group."""
        return self.students.count()

    def get_students(self):
        """Returns a list of students in the group."""
        return self.students.all()
