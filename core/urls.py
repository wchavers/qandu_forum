from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^user/', include('registration.backends.simple.urls')),
    url(r'^user/', include('django.contrib.auth.urls')),
    url(r'^forum/create/$', login_required(ForumCreateView.as_view()), name='forum_create'),
    url(r'forum/$', login_required(ForumListView.as_view()), name='forum_list'),
    url(r'^forum/(?P<pk>\d+)/$', login_required(ForumDetailView.as_view()), name='forum_detail'),
    url(r'^forum/update/(?P<pk>\d+)/$', login_required(ForumUpdateView.as_view()), name='forum_update'),
    url(r'^forum/delete/(?P<pk>\d+)/$', login_required(ForumDeleteView.as_view()), name='forum_delete'),
    url(r'^forum/(?P<pk>\d+)/answer/create/$', login_required(ForumCreateView.as_view()), name='answer_create'),
    url(r'^forum/(?P<forum_pk>\d+)/answer/update/(?P<answer_pk>\d+)/$', login_required(AnswerUpdateView.as_view()), name='answer_update'),
    url(r'^forum/(?P<forum_pk>\d+)/answer/delete/(?P<answer_pk>\d+)/$', login_required(AnswerDeleteView.as_view()), name='answer_delete'),
)