from django.urls import path
from edu import views

urlpatterns = [
    path("students/", views.StudentListView.as_view(), name="student-list"),
    path("students/<int:id>/", views.StudentDetailView.as_view(), name="student-detail"),
    path("courses/", views.CourseListView.as_view(), name="course-list"),
    path("courses/<int:id>/", views.CourseDetailView.as_view(), name="course-detail"),
    path("employees/", views.EmployeeListView.as_view(), name="employee-list"),
    path("employees/<int:id>/", views.EmployeeDetailView.as_view(), name="employee-detail"),
    path("groups/", views.GroupListView.as_view(), name="group-list"),
    path("groups/<int:id>/", views.GroupDetailView.as_view(), name="group-detail"),
    path("students/<int:id>/update_balance/", views.UpdateBalanceView.as_view(), name="update-balance"),

]
