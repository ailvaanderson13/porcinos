from django.contrib import admin
from django.urls import path, include
from apps.utils import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('apps.utils.urls', 'utils'), namespace='utils')),
    path('category/', include(('apps.categoria.urls', 'categoria'), namespace='categoria')),
    path('cliente/', include(('apps.cliente.urls', 'cliente'), namespace='cliente')),
    path('item/', include(('apps.item.urls', 'item'), namespace='item')),
    path('pedido/', include(('apps.pedido.urls', 'pedido'), namespace='pedido')),
    path('company/', include(('apps.company.urls', 'company'), namespace='company')),
    path('user/', include(('apps.user.urls', 'user'), namespace='user')),
    path('store/', include(('apps.store.urls', 'store'), namespace='store')),
]
