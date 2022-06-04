from django.urls import path
from . import views


urlpatterns = [
    path('new-cliente/', views.cadastro_update_cliente, name="new-cliente"),
    path('edit-cliente/<int:pk>', views.cadastro_update_cliente, name="edit-cliente"),
    path('list-cliente/', views.list_cliente, name="list-cliente"),
    path('delete/', views.delete_cliente, name="delete"),
]
