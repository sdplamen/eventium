from django.urls import path
from event import views

urlpatterns = [

    path('', views.EventListView.as_view(), name='events'),
    # path('', views.event_list, name='event-list'),
    path('create/', views.EventCreateView.as_view(), name='create-event'),
    # path('create/', views.create_event, name='event-create'),
    path('<int:event_pk>/details/', views.EventDetailView.as_view(), name='details-event'),
    # path('<int:event_pk>/details/', views.event_details, name='event-details'),
    path('<int:event_pk>/edit/', views.EventUpdateView.as_view(), name='edit-event'),
    # path('<int:event_pk>/edit/', views.edit_event, name='event-edit'),
    path('<int:event_pk>/delete/', views.EventDeleteView.as_view(), name='delete-event'),
    # path('<int:event_pk>/delete/', views.delete_event, name='event-delete'),
]