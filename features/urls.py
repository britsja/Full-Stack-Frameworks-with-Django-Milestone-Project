from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_open_features, name="show_open_features"),
    path('open_feature/<id>', views.show_feature, name="open_feature"),
    path('add_feature_comment/<id>', views.add_feature_comment, name="add_feature_comment"),
    path('add_feature/', views.add_feature, name="add_feature"),
    path('upvote_request/<id>', views.upvote_request, name="upvote_request"),
    path('close_feature/<id>', views.close_feature, name="close_feature"),
    path('reopen_feature/<id>', views.reopen_feature, name="reopen_feature"),
    
]
