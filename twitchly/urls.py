from django.conf.urls import patterns, url

from twitchly import views

urlpatterns = patterns('',
    # ex: /twitchly/
    url(r'^$', views.index, name='index'),
    url(r'^invite$', views.BetaInviteCreate.as_view(), name='invite'),
    url(r'^thanks$', views.invite_thanks, name='invite_thanks'),
    # ex: /polls/5/
    #url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)