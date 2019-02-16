from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .models import Ticket, Comments
from .forms import CommentsForm

def show_open_tickets(request):
    tickets = Ticket.objects.all()
    return render(request, 'showtickets.html', {'tickets': tickets})

def show_ticket(request, id):
    ticket = get_object_or_404(Ticket, pk=id)
    comments = Comments.objects.filter(ticket = id).values()
    return render(request, "openticket.html",{'ticket': ticket, 'comments': comments})

def add_comment(request, id):
    ticket = get_object_or_404(Ticket, pk=id)

    if request.method == "POST":
        form = CommentsForm(request.POST, request.FILES, instance=ticket)

        if form.is_valid():
            comment = form.save()
            return redirect(show_open_ticket, id)
    else:
        form = CommentsForm(instance=ticket)

    return render(request, "addcomment.html",{'form': form})
   