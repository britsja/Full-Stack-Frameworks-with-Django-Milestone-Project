from django.shortcuts import render

def show_open_tickets(request):
    return render(request, 'showtickets.html')