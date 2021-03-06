from django.conf.urls import patterns, include, url
from django.contrib import admin
from lib.auth import views as auth_views
from django.conf import settings

admin.autodiscover()

urlpatterns = [
    url(r'^auth/', include('lib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^landing/', include('lib.landing.urls')),
    url(r'^', include('lib.main.urls')),
    url(r'^', include('lib.photo.urls')),
    url(r'^map/', include('lib.map.urls')),
]
