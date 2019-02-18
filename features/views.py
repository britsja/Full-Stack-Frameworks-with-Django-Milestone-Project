from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .models import Features, FeatureComments
from .forms import CommentsForm, FeaturesForm
from django.contrib.auth.models import User
from datetime import datetime

def show_open_features(request):
    features = Features.objects.all()
    return render(request, 'featurerequests.html', {'features': features})

def show_feature(request, id):
    feature = get_object_or_404(Features, pk=id)
    comments = FeatureComments.objects.filter(feature = id).values()
    users = User.objects.all()
    current_user = request.user

    return render(request, "openfeature.html",{'feature': feature, 'users': users, 'current_user': current_user, 'comments': comments})

def add_feature_comment(request, id):
    feature = get_object_or_404(Features, pk=id)
    current_user = request.user
    

    if request.method == "POST":
        form = CommentsForm(request.POST or None)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.commentusername = request.user
            comment.feature = feature
            comment.created_date = datetime.now()
            comment.save()
            return redirect(show_feature, id)
            
    else:
        form = CommentsForm(instance=feature)

    return render(request, "addfeaturecomment.html",{'form': form})

def add_feature(request):
    current_user = request.user

    if request.method == "POST":
        form = FeaturesForm(request.POST or None)
        

        if form.is_valid():
            feature = form.save(commit=False)
            feature.featureusername = current_user
            feature.created_date = datetime.now()
            feature.status = True
            feature.upvotes = 0
            feature.save()
            return redirect(show_open_features)

    else:
        form = FeaturesForm()

    return render(request, "addfeature.html", {'form': form})

def upvote_request(request, id):
    feature = get_object_or_404(Features, pk=id)
    feature.upvotes += 1
    feature.save()

    return redirect(show_feature, id)

def close_feature(request, id):
    feature = get_object_or_404(Features, pk=id)
    feature.status = False
    feature.save()

    return redirect(show_open_features)

def reopen_feature(request, id):
    feature = get_object_or_404(Features, pk=id)
    feature.status = True
    feature.save()

    return redirect(show_open_features)