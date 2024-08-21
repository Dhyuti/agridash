from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # API routes
    path('', include('api.frontend_urls')),  # HTML routes
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
