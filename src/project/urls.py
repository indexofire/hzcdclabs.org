# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from feincms.module.page.sitemap import PageSitemap

admin.autodiscover()

sitemaps = {'page': PageSitemap,}

# admin and admin docs
urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

# create sitemap
urlpatterns += patterns('',
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps}
    ),
)

# django static serve in DEBUG mode
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.strip('/'),
            'django.views.static.serve', {'document_root': settings.MEDIA_ROOT},
        ),
    )

# default url route
urlpatterns += patterns('',
    url(r'^', include('feincms.urls')),
)
