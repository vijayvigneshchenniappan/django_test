from django.conf.urls import patterns, include, url
from django_test.views import hello, hello_template, hello_template_simple, login, auth_view, logout, loggedin, \
    invalid_login,register_user, register_success

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'django_test.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),

                       ###################
                       url(r'^hello$', hello),
                       url(r'^hello_template$', hello_template),
                       url(r'^hello_template_simple$', hello_template_simple),  #Advanced Url

                       (r'^articles/', include('article.urls')),

                       #Auth URL

                       url(r'^accounts/login/$', login),
                       url(r'^accounts/auth/$', auth_view),
                       url(r'^accounts/logout/$', logout),
                       url(r'^accounts/loggedin/$', loggedin),
                       url(r'^accounts/invalid/$', invalid_login),
                       url(r'^accounts/register/$', register_user),
                       url(r'^accounts/register_success/$', register_success),
)
