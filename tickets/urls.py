from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_open_tickets, name="show_open_tickets"),
    path('show_ticket/<id>', views.show_ticket, name="show_ticket"),
    path('add_comment/<id>', views.add_comment, name="add_comment"),
    path('add_ticket', views.add_ticket, name="add_ticket" ),
    path('close_ticket/<id>', views.close_ticket, name="close_ticket"),
    path('reopen_ticket/<id>', views.reopen_ticket, name="reopen_ticket"),
    path('show_closed_tickets/', views.show_closed_tickets, name="show_closed_tickets")
]
