from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .models import Features
#from .forms import CommentsForm, TicketsForm
from django.contrib.auth.models import User
from datetime import datetime

def show_open_features(request):
    features = Features.objects.all()
    return render(request, 'featurerequests.html', {'features': features})

def show_feature(request, id):
    feature = get_object_or_404(Features, pk=id)
    #comments = Comments.objects.filter(ticket = id).values()
    users = User.objects.all()
    current_user = request.user

    return render(request, "openfeature.html",{'feature': feature, 'users': users, 'current_user': current_user})