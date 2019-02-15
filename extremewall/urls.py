from django.contrib import admin
from django.urls import include, path
from home.views import index
from tickets import urls
from accounts import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('tickets/', include('tickets.urls')),
    path('accounts/', include('accounts.urls')),
]

