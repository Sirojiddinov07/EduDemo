from django.db.models import QuerySet
from edu.models import Employee

class EmployeeService:
    @staticmethod
    def get_all_employees() -> QuerySet:
        """Returns all employees."""
        return Employee.objects.all()

    @staticmethod
    def get_employee_by_id(employee_id: int) -> Employee | None:
        """Returns an employee by ID."""
        return Employee.objects.get(id=employee_id)
