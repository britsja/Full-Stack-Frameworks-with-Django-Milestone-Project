from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_cart, name="show_cart"),
    path('add/<id>', views.add_cart, name="add_cart"),
    path('remove/<id>', views.remove_item, name="remove_item")
]