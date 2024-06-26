from django.urls import path
from .views import *

urlpatterns = [
        path('school/create/', SchoolCreateView.as_view(), name='school_create'),
        path('school/profile/<int:pk>/', SchoolProfileView.as_view(), name='fetch_school_profile'),
        path('school/profile/update/<int:pk>/', SchoolProfileUpdateView.as_view(), name='schedule_update'),
        path('school/profile/', SchoolAdminProfileView.as_view(), name='schedule_profile'),
        path('school/list/', SchoolAdminListView.as_view(), name='school_list'),
        path('school/delete/<int:pk>/', SchoolAdminDeleteView.as_view(), name='school_delete'),
        path('profile/', SuperAdminProfile.as_view(), name='super_admin_profile'),

        # Curriculum API
        path('curriculum/create/', CurriculumCreateView.as_view(), name='curriculum_create'),
        path('curriculum/list/', CurriculumListView.as_view(), name='curriculum_list'),
        path('curriculum/detail/<int:pk>/', CurriculumDetailView.as_view(), name='curriculum_detail'),
        path('curriculum/update/<int:pk>/', CurriculumUpdateView.as_view(), name='curriculum_update'),
        path('curriculum/delete/<int:pk>/', CurriculumDeleteView.as_view(), name='curriculum_delete'),

        # Book Related API
        path('book/content/list/', BookContentList.as_view(), name='book_content_list'),
        path('book/update/<int:pk>/', BookContentUpdateView.as_view(), name='content_update'),
        path('book/detail/<int:pk>/', BookContentDetailView.as_view(), name='content_detail'),
        path('book/delete/<int:pk>/', BookContentDeleteView.as_view(), name='content_delete'),

        # Inquiry Related API'S
        path('inquiry/list/', InquiryListView.as_view(), name='inquiry_list'),
        path('inquiry/detail/<int:pk>/', InquiryDetailView.as_view(), name='inquiry_detail'),
]