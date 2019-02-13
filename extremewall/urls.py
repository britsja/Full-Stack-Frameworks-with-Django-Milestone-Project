from django.contrib import admin
from django.urls import path
from home.views import index
from tickets.views import show_open_tickets

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('tickets/', show_open_tickets, name='show_open_tickets')
]

