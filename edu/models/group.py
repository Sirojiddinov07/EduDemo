from django.db import models
from edu.models import AbstractModel, Student


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
