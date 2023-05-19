from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('openapi.json', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path("api/", include('api.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
        *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ]
