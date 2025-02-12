from rest_framework.permissions import BasePermission
from edu.models import Employee

class IsManager(BasePermission):
    def has_permission(self, request, view):
        if not hasattr(request.user, 'employee'):
            return False
        return request.user.employee.role == Employee.ROLE_MANAGER

class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        if not hasattr(request.user, 'employee'):
            return False
        return request.user.employee.role == Employee.ROLE_TEACHER

class IsStaff(BasePermission):
    def has_permission(self, request, view):
        if not hasattr(request.user, 'employee'):
            return False
        return request.user.employee.role == Employee.ROLE_STAFF
