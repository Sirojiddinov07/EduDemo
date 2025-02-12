from django.contrib.auth.models import User
from django.db import models

class Employee(models.Model):
    ROLE_ADMIN = 1
    ROLE_MANAGER = 2
    ROLE_TEACHER = 3
    ROLE_STAFF = 4

    ROLE_CHOICES = (
        (ROLE_ADMIN, "Admin"),
        (ROLE_MANAGER, "Manager"),
        (ROLE_TEACHER, "Teacher"),
        (ROLE_STAFF, "Staff"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField(choices=ROLE_CHOICES, default=ROLE_STAFF)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"
