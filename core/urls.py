from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^user/', include('registration.backends.simple.urls')),
    url(r'^user/', include('django.contrib.auth.urls')),
    url(r'^forum/create/$', ForumCreateView.as_view(), name='forum_create'),
    url(r'forum/$', ForumListView.as_view(), name='forum_list'),
    url(r'^forum/(?P<pk>\d+)/$', ForumDetailView.as_view(), name='forum_detail'),
    url(r'^forum/update/(?P<pk>\d+)/$', ForumUpdateView.as_view(), name='forum_update'),
    url(r'^forum/delete/(?P<pk>\d+)/$', ForumDeleteView.as_view(), name='forum_delete'),
    url(r'^forum/(?P<pk>\d+)/answer/create/$', AnswerCreateView.as_view(), name='answer_create'),
)