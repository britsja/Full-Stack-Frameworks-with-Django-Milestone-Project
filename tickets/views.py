from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .models import Ticket, Comments
from .forms import CommentsForm
from django.contrib.auth.models import User

def show_open_tickets(request):
    tickets = Ticket.objects.all()
    return render(request, 'showtickets.html', {'tickets': tickets})

def show_ticket(request, id):
    ticket = get_object_or_404(Ticket, pk=id)
    comments = Comments.objects.filter(ticket = id).values()
    users = User.objects.all()
    
    return render(request, "openticket.html",{'ticket': ticket, 'comments': comments, 'users': users})

def add_comment(request, id):
    ticket = get_object_or_404(Ticket, pk=id)
    comments = get_list_or_404(Comments, ticket = ticket.id)
    current_user = request.user
    

    if request.method == "POST":
        form = CommentsForm(request.POST or None)
        print(form)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.commentusername = request.user
            comment.save()
            tickets = Ticket.objects.all()
            comments = Comments.objects.filter(ticket = id).values()
            users = User.objects.all()
            return render(request, "openticket.html",{'ticket': ticket, 'comments': comments, 'users': users})
            
    else:
        form = CommentsForm(instance=ticket)

    return render(request, "addcomment.html",{'form': form})
   