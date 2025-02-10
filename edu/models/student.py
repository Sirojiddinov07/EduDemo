from django.db import models
from edu.models import AbstractModel

class Student(AbstractModel):
    STATUS_WAITING = 1
    STATUS_ACTIVE = 2
    STATUS_LEFT = 3

    STATUS_CHOICES = (
        (STATUS_WAITING, "Waiting"),
        (STATUS_ACTIVE, "Active"),
        (STATUS_LEFT, "Left"),
    )

    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, unique=True)
    balance = models.IntegerField(default=0)
    status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_WAITING)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ["-id"]

    def __str__(self):
        return f"{self.full_name} - {self.status}"
