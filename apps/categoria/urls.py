from django.urls import path
from . import views


urlpatterns = [
    path('new-category/', views.new_category, name="new-category"),
    path('edit-category/<int:pk>', views.new_category, name="edit-category"),
    path('list-category/', views.list_categoria, name="list-category"),
    path('delete/', views.delete_categoria, name="delete")
]