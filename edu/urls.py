from django.urls import path
from edu import views
urlpatterns = [
    path("students/", views.StudentListView.as_view(), name="student-list"),
    path("students/<int:id>/", views.StudentDetailView.as_view(), name="student-detail"),
]
