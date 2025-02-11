from django.db.models import QuerySet
from edu.models import Group

class GroupService:
    @staticmethod
    def get_all_groups() -> QuerySet:
        """Returns all groups with related course, instructor, and students."""
        return Group.objects.select_related("course", "instructor").prefetch_related("students").all()

    @staticmethod
    def get_group_by_id(group_id: int) -> Group | None:
        """Returns a single group by ID with related course, instructor, and students."""
        return Group.objects.select_related("course", "instructor").prefetch_related("students").get(id=group_id)
