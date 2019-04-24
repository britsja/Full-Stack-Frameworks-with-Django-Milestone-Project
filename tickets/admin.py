from django.contrib import admin
#from .models import Ticket_username, Ticket, Ticketcategory, Comments
from .models import Ticket, Ticketcategory, Comments

#admin.site.register(Ticket_username)
admin.site.register(Ticket)
admin.site.register(Ticketcategory)
admin.site.register(Comments)