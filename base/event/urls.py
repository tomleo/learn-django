from django.conf.urls import patterns, url

from event.views import detailv, listv, editv, addv

urlpatterns = patterns('',
    url(r'^$', listv.as_view(), name='event-list'),
    url(r'^add/$', addv.as_view(), name='event-add'),
    url(r'^edit/$', editv.as_view(), name='event-edit'),
    url(r'^detail/(\d{4})/$', detailv.as_view(), name='event-detail'),
)
