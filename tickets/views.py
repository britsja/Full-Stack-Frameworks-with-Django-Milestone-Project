from django.shortcuts import render, get_object_or_404
from .models import Ticket, Comments

def show_open_tickets(request):
    tickets = Ticket.objects.all()
    return render(request, 'showtickets.html', {'tickets': tickets})

def show_ticket(request, id):
    ticket = get_object_or_404(Ticket, pk=id)
    comments = Comments.objects.filter(ticket = id).values()
    return render(request, "openticket.html",{'ticket': ticket, 'comments': comments})