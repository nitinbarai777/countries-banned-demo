from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.urls import path
from project.urls.sites.api import router
from countrybanned.core import views as api_views
from countrybanned.core import views as api_views
from django.views.static import serve


urlpatterns = [
    url(r'^', include('project.urls.root')),
    url(r'^$', api_views.home, name='home'),
    url(r'^api/', include(router.urls)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT, }),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
