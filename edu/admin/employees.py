from django.contrib import admin
from edu.models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "phone", "role")
    list_filter = ("role",)
    search_fields = ("full_name", "phone")