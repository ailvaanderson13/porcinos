from django.urls import path
from . import views
from apps.utils.views import dashboard_admin

urlpatterns = [
    path('new-store/', views.create_update_store, name="new-store"),
    path('edit-store/<int:pk>/', views.create_update_store, name="edit-store"),
    path('list-store/', views.panel_store, name="list-store"),
    path('delete-store/', views.delete_store, name="delete-store"),
]