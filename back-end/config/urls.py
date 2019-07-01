from rest_framework.schemas import get_schema_view

from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin

schema_view = get_schema_view(title='App API')


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path(r'', include(('app.urls', 'apps'), namespace='apps')),
    path(r'schema/', schema_view),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
