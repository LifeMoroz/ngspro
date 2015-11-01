from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns('lib.mapbaloon.views',
        url(r'^upload/$', views.upload),
        url(r'^ulavatar/$', views.upload_avatar, name='upload-avatar'),
        url(r'^ulmaterial/$', views.upload_material, name='upload-material'),
)
