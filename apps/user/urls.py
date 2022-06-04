from django.urls import path
from . import views

urlpatterns = [
    path('new-user/', views.create_update_user, name='new-user'),
    path('edit-user/<int:pk>/', views.create_update_user, name='edit-user'),
    path('list-user/', views.list_user, name='list-user'),
    path('delete-user/', views.delete_user, name="delete-user"),
    path('edit-my-profile/', views.my_profile, name="my-profile"),
]