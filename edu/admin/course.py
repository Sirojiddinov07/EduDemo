from django.contrib import admin
from edu.models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price")
    search_fields = ("title",)
    list_filter = ("price",)
