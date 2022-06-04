from django.urls import path
from . import views

urlpatterns = [
    path('new-company/', views.create_update_company, name="new-company"),
    path('edit-company/<int:pk>/', views.create_update_company, name="edit-company"),
    path('delete-company/', views.delete_company, name="delete-company"),
    path('list-company/', views.list_company, name="list-company")
]   