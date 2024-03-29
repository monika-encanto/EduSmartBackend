from django.urls import path
from .views import *

urlpatterns = [
        path('teacher/users/create/', TeacherUserCreateView.as_view(), name='teacher_user_create'),
        path('fetch/teacher/detail/<int:pk>/', FetchTeacherDetailView.as_view(), name='fetch_student_detail'),
        path('teacher/list/', TeacherListView.as_view(), name='student_list'),
        path('teacher/delete/<int:pk>/', TeacherDeleteView.as_view(), name='teacher_delete'),
        path('teacher/update-profile/<int:pk>/', TeacherUpdateProfileView.as_view(), name='update_teacher_profile'),
]