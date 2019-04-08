from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_cart, name="show_cart"),
    path('add/<id>', views.add_cart, name="add_cart"),
    path('edit/<id>', views.edit_cart, name="edit_cart")
]