from django.urls import path
from organiser import views


urlpatterns = [
    path('create/', views.OrganizerCreateView.as_view(), name='create-organizer'),
    # path('create/', views.create_organizer, name='organizer-create'),
    path('details/', views.OrganizerDetailView.as_view(), name='details-organizer'),
    # path('details/', views.organizer_details, name='organizer-details'),
    path('edit/', views.OrganizerUpdateView.as_view(), name='edit-organizer'),
    # path('edit/', views.edit_organizer, name='organizer-edit'),
    path('delete/', views.OrganizerDeleteView.as_view(), name='delete-organizer'),
    # path('delete/', views.delete_organizer, name='organizer-delete'),
]