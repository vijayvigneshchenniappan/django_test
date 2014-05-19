from django.conf.urls import patterns, include, url
from article.views import sample_advanced_url, article, articles, language, create
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',

                       url(r'^all$', articles),
                       url(r'^get/(?P<article_id>\d+)/$', article),
                       url(r'^language/(?P<language>[a-z\-]+)/$', language),
                       url(r'^advancedurl$', sample_advanced_url),
                       url(r'^advancedurl$', sample_advanced_url),
                       url(r'^create', create),

)
