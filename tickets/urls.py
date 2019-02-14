from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_open_tickets, name="show_open_tickets")
]
