from django.conf.urls import patterns, url

urlpatterns = patterns('faq.views',

    url(regex=r'^$',
        view='faq_list',
        name='faq_list'),
)
