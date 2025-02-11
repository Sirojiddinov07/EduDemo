from celery import shared_task
from edu.models import Student


@shared_task
def deduct_student_balance():
    students = Student.objects.prefetch_related("groups").all()

    for student in students:
        courses = {group.course for group in student.groups.all()}  # Get unique courses
        total_price = sum(course.price for course in courses)

        student.balance -= total_price
        student.save()
    return f"Deducted balance for {students.count()} students"
