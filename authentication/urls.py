from django.urls import path

from .admin_views import *
from .views import *

urlpatterns = [
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/login/', LoginView.as_view(), name='user_login'),
    path('fetch/user/detail/<int:pk>/', FetchUserDetailView.as_view(), name='fetch_user_detail'),
    path('users/list/', UsersList.as_view(), name='users_list'),
    path('user/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
    path('user/update-profile/', UserUpdateProfileView.as_view(), name='update_profile'),

    # Admin Panel APIS
    path('staff/login/', AdminStaffLoginView.as_view(), name='staff_login'),
    path('staff/create/', AdminStaffCreateView.as_view(), name='staff_create'),
    path('staff/list/', StaffListView.as_view(), name='staff_list'),
    path('staff/get-profile/', StaffProfileView.as_view(), name='staff_profile'),
    path('staff/get-profile/<int:pk>/', GetStaffView.as_view(), name='get_staff'),
    path('staff/update-profile/<int:pk>/', StaffUpdateProfileView.as_view(), name='staff_update_profile'),
    path('staff/delete/<int:pk>/', AdminStaffDeleteView.as_view(), name='staff_delete'),

    # Non teaching staff APIS
    path('non-teaching-staff/create/', NonTeachingStaffCreateView.as_view(), name='staff_create'),
    path('non-teaching-staff/fetch/list/', NonTeachingStaffListView.as_view(), name='staff_list'),
    path('non-teaching-staff/fetch/detail/<int:pk>/', NonTeachingStaffDetailView.as_view(), name='staff_detail'),
    path('non-teaching-staff/delete/<int:pk>/', NonTeachingStaffDeleteView.as_view(), name='staff_delete'),
    path('non-teaching-staff/update/<int:pk>/', NonTeachingStaffUpdateView.as_view(), name='staff_update'),

    # Non-teaching staff attendence API's
    path('attendance/create/', AttendanceCreateView.as_view(), name='attendance_create'),
    path('attendance/detail/<int:pk>/', FetchAttendanceDetailView.as_view(), name='fetch_attendance_detail'),
    path('attendance/list/',  FetchAttendanceListView.as_view(), name='fetch_attendance_list'),

    # Notification
    path('notification/create/', NotificationCreateView.as_view(), name='notification_create'),
    path('notification/get/', NotificationListView.as_view(), name='notification_get'),
    path('notification/clear/', NotificationDeleteView.as_view(), name='notification_delete'),

    # Announcement
    path('announcement /create/', AnnouncementCreateView.as_view(), name='announcement_create'),
    path('announcement /list/', AnnouncementListView.as_view(), name='announcement_create'),

    #Mobile App
    path('users/logout/', LogoutView.as_view(), name='user_logout'),
    path('user/profile/', UserProfileView.as_view(), name='user_profile'),
    path('teacher/schedule/', TeacherUserScheduleView.as_view(), name='teacher_user_schedule'),
    path('curriculum/list/', TeacherCurriculumListView.as_view(), name='teacher_curriculum_list'),
    path('teacher/day/review/', TeacherDayReviewView.as_view(), name='teacher_day_review'),
    path('teacher/day/review/detail/<int:pk>/', TeacherDayReviewDetailView.as_view(), name='teacher_day_review_detail'),
    path('teacher/day/review/list/', TeacherDayReviewListView.as_view(), name='teacher_day_review_list'),
    path('teacher/attendance/', FetchTeacherAttendanceView.as_view(), name='fetch_teacher_attendance')
]