from django.urls import path
from .views import ContentCreateView, ContentListView, ContentDeleteView, SuperAdminContentCreateView

urlpatterns = [
    path('super-admin/create/', SuperAdminContentCreateView.as_view(), name='super-admincontent-create'),
    path('create/', ContentCreateView.as_view(), name='content-create'),
    path('get-all-data/', ContentListView.as_view(), name='get-all-content-data'),
    path('delete/<int:pk>/', ContentDeleteView.as_view(), name='content-delete'),
]