from django.contrib import admin
from edu.models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "phone", "balance", "status")
    list_filter = ("status",)
    search_fields = ("full_name", "phone")
    ordering = ("-id",)
