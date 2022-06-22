from django.urls import path
from . import views

urlpatterns = [
    path('new-pedido/', views.create_update_pedido, name="new-pedido"),
    path('sales_today/', views.sales_today, name="sales-today"),
    path('sales_money/', views.sales_money, name="sales-money"),
    path('sales_pix/', views.sales_pix, name="sales-pix"),
    path('sales_card/', views.sales_card, name="sales-card"),
    path('open-new-pedido/', views.safe_pedido, name="open-new-pedido"),
    path('edit-pedido/<int:pk>', views.create_update_pedido, name="edit-pedido"),
    path('list-pedido/', views.list_pedidos, name="list-pedido"),
    path('detail-pedido/', views.detail_pedido, name="detail-pedido"),
    path('checkout/get_product/', views.get_product, name="get_product"),

]