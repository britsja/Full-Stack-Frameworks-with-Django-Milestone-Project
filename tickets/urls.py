from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_open_tickets, name="show_open_tickets"),
    path('show_ticket/<id>', views.show_ticket, name="show_ticket")
]
