from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, reverse
from django.shortcuts import redirect


urlpatterns = [
    path("dj-admin/", admin.site.urls),
    path("auth/", include("authentication.urls")),
    path("", lambda _: redirect(reverse("dashboard"))),
    path("dashboard/", include("modules.dashboards.urls")),
    path("users/", include("modules.accounts.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
