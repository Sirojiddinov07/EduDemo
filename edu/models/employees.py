from django.db import models
from edu.models import AbstractModel

class Employee(AbstractModel):
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

    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, unique=True)
    role = models.IntegerField(choices=ROLE_CHOICES, default=ROLE_STAFF)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return f"{self.full_name} - {self.role}"

