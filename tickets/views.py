from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .models import Ticket, Comments, Ticketcategory
from .forms import CommentsForm, TicketsForm
from django.contrib.auth.models import User
from datetime import datetime

def show_open_tickets(request):
    tickets = Ticket.objects.all()
    return render(request, 'showtickets.html', {'tickets': tickets})

def show_ticket(request, id):
    ticket = get_object_or_404(Ticket, pk=id)
    comments = Comments.objects.filter(ticket = id).values()
    users = User.objects.all()
    current_user = request.user
    
    return render(request, "openticket.html",{'ticket': ticket, 'comments': comments, 'users': users, 'current_user': current_user})

def add_comment(request, id):
    ticket = get_object_or_404(Ticket, pk=id)
    current_user = request.user
    

    if request.method == "POST":
        form = CommentsForm(request.POST or None)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.commentusername = request.user
            comment.ticket = ticket
            comment.created_date = datetime.now()
            comment.save()
            return redirect(show_ticket, id)
            
    else:
        form = CommentsForm(instance=ticket)

    return render(request, "addcomment.html",{'form': form})
   
def add_ticket(request):
    category = Ticketcategory.objects.all()
    current_user = request.user

    if request.method == "POST":
        form = TicketsForm(request.POST or None)
        

        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.ticketusername = current_user
            ticket.created_date = datetime.now()
            ticket.status = True
            ticket.save()
            return redirect(show_open_tickets)

    else:
        form = TicketsForm()

    return render(request, "addticket.html", {'form': form, 'category' : category})

def close_ticket(request, id):
    ticket = get_object_or_404(Ticket, pk=id)
    ticket.status = False
    ticket.closed_date = datetime.now()
    ticket.save()

    tickets = Ticket.objects.all()
    return redirect(show_open_tickets)

def reopen_ticket(request, id):
    ticket = get_object_or_404(Ticket, pk=id)
    ticket.status = True
    ticket.closed_date = None
    ticket.save()

    tickets = Ticket.objects.all()
    return redirect(show_open_tickets)