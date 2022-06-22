from django.urls import path
from . import views

urlpatterns = [
    path('reposicao/', views.menos_itens, name="reposicao-produto"),
    path('new-produto/', views.create_update_item, name="new-produto"),
    path('edit-produto/<int:pk>', views.create_update_item, name="edit-produto"),
    path('list-produto/', views.list_item, name="list-produto"),
    path('delete/', views.delete_item, name="delete")
]
