from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_open_features, name="show_open_features"),
    path('open_feature/<id>', views.show_feature, name="open_feature"),
    
]
