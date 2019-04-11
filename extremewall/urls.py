from django.contrib import admin
from django.urls import include, path
from home.views import index, stats
from tickets import urls
from accounts import urls
from features import urls
from cart import urls
from checkout import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('tickets/', include('tickets.urls')),
    path('accounts/', include('accounts.urls')),
    path('features/', include('features.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('stats/', stats, name='stats')
    
]

