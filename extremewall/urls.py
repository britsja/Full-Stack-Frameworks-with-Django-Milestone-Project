from django.contrib import admin
from django.urls import path
from extremewall import views
from home.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index)
]

