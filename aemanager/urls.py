from django.conf.urls import patterns, include, url

from django.conf import settings
from core.views import resend_activation_email, contact_us

from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    
    url(regex=r'^$',
        view='core.views.index',
        name='index'),
    url(regex=r'^contact_us/$',
        view=contact_us,
        name='contact_us'),
    url(r'^contact/sent/$', TemplateView.as_view(template_name='core/message_sent.html'), name='message_sent'),
    url(regex=r'^logout/$',
        view='django.contrib.auth.views.logout',
        name='logout',
        kwargs={'next_page': '/'}),
    url(regex=r'^resend_activation_email/$',
        view=resend_activation_email,
        name='resend_activation_email'),
    url(r'^tos/$',  TemplateView.as_view(template_name='tos.html'), name='tos'),
    url(r'^changelog/$', TemplateView.as_view(template_name='changelog.html'), name='changelog'),
    url(r'^home/', include('core.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^project/', include('project.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^issues/', include('bugtracker.urls')),
    ##url(r'^user/', include('registration_urls')),
    url(r'^user/', include('registration.auth_urls')),
    
    url(r'^newsletter/', include('newsletter.urls')),
    url(r'^backup/', include('backup.urls')),
    url(r'^faq/', include('faq.urls')),
    url(r'^forum/', include('forum.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )
