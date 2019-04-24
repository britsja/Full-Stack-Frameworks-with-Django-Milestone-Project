from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .models import Features, FeatureComments
from .forms import CommentsForm, FeaturesForm
from django.contrib.auth.models import User
from datetime import datetime

# Show all open features
def show_open_features(request):
    features = Features.objects.all()
    feature_page = "active"
    return render(request, 'featurerequests.html', {'features': features, 'feature_page': feature_page})

# Open a specific feature by id passing through user details too
def show_feature(request, id):
    feature = get_object_or_404(Features, pk=id)
    comments = FeatureComments.objects.filter(feature = id).values()
    users = User.objects.all()
    current_user = request.user
    voted = False
    feature_page = "active"
    if request.session.get('voted', False):
        voted = True

    return render(request, "openfeature.html",{'feature': feature, 'users': users, 'current_user': current_user, 'comments': comments, 'voted': voted, 'feature_page': feature_page})

# Create a feature comment on feature id
def add_feature_comment(request, id):
    feature = get_object_or_404(Features, pk=id)
    current_user = request.user
    feature_page = "active"

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

    return render(request, "addfeaturecomment.html",{'form': form, 'feature_page': feature_page})

# Create a new feature request
def add_feature(request):
    current_user = request.user
    feature_page = "active"

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

    return render(request, "addfeature.html", {'form': form, 'feature_page': feature_page})

# Close selected feature, open only given to admin or feature creator
def close_feature(request, id):
    feature = get_object_or_404(Features, pk=id)
    feature.status = False
    feature.closed_date = datetime.now()
    feature.save()

    return redirect(show_open_features)

# Reopen selected feature - option only given to admin or feature creator
def reopen_feature(request, id):
    feature = get_object_or_404(Features, pk=id)
    feature.status = True
    feature.closed_date = None
    feature.save()

    return redirect(show_open_features)

# Display closed features
def closed_features(request):
    features = Features.objects.all()
    feature_page = "active"

    return render(request, 'closedfeatures.html', {'features': features, 'feature_page': feature_page})

# Upvote a feature (NOT PURCHASE)    
def upvote_request(request, id):
    if request.session.get('voted', False):
        return
    else:
        feature = get_object_or_404(Features, pk=id)
        feature.upvotes += 1
        feature.save()
        request.session['voted'] = True

    return redirect(show_feature, id)