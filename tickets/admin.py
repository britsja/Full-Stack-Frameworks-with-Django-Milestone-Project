from django.contrib import admin
from .models import Ticket_username, Ticket, Ticketcategory

admin.site.register(Ticket_username)
admin.site.register(Ticket)
admin.site.register(Ticketcategory)