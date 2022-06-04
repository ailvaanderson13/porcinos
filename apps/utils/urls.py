from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard_admin, name="dashboard_admin"),
    path('login/', views.acesso, name="login"),
    path('logout/', views.logout_, name="logout"),
    path('onload/card/', views.load_dashboard, name="load_dash"),
    path('checkout/', views.checkout, name="checkout"),
]