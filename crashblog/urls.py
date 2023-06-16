from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from .sitemaps import CategorySitemap, PostSitemap
from core.views import robots_txt

sitemaps = {"category": CategorySitemap, "post": PostSitemap}

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}),
    path("robots.txt", robots_txt, name="robots.txt"),
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("", include("blog.urls")),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
