from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from clients.views import profile_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', profile_view, name='profile'),
    path('cart/', include('shopping_list.urls', namespace='cart')),
    path('', include('literature.urls', namespace='literature')),
        
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
