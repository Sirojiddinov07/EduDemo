from django.contrib import admin
from edu.models import Group

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "course", "instructor")
    search_fields = ("name", "course__title", "instructor__full_name")
    list_filter = ("course", "instructor")
    filter_horizontal = ("students",)
