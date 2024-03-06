from django.urls import include, path
from . import views


app_name = "warehouse"

urlpatterns = [
    path("", views.index, name="index"),
    path("inventory/", views.index, name="inventory"),
    path("orders/", views.orders, name="orders"),
    path("orders/new/", views.new_order, name="new_order"),
    # path('new_delivery', views.new_delivery, name='new_delivery'),
]
