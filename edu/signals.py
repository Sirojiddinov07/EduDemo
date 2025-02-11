from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from edu.models import Group, Student

@receiver(m2m_changed, sender=Group.students.through)
def update_student_status(sender, instance, action, pk_set, **kwargs):
    """
    Updates student status based on group membership changes.
    """
    if action in ["post_add"]:
        Student.objects.filter(id__in=pk_set).update(status=Student.STATUS_ACTIVE)
    elif action in ["post_remove"]:
        Student.objects.filter(id__in=pk_set).update(status=Student.STATUS_LEFT)
