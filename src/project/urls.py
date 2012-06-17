# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from feincms.module.page.sitemap import PageSitemap

admin.autodiscover()

# create sitemap
sitemaps = {
    'page': PageSitemap,
}

urlpatterns = patterns('',
    # url(r'^$', 'cdclabs.views.home', name='home'),
    # url(r'^cdclabs/', include('cdclabs.foo.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', 
        {'sitemaps': sitemaps}
    ),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.strip('/'),
            'django.views.static.serve', {'document_root': settings.MEDIA_ROOT},
        ),
    )

# 
urlpatterns += patterns('',
    url(r'', include('feincms.urls')),
)
