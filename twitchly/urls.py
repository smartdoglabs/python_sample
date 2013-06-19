from django.conf.urls import patterns, url
from twitchly.authentication import TwitchlyLoginForm
from twitchly import views

urlpatterns = patterns('',
    # ex: /twitchly/
    url(r'^$', views.index, name='index'),
    url(r'^invite$', views.BetaInviteCreate.as_view(), name='invite'),
    url(r'^thanks$', views.invite_thanks, name='invite_thanks'),
    
    url(r'^login/$', 'django.contrib.auth.views.login', {'authentication_form':TwitchlyLoginForm,'template_name': 'twitchly/security/login.html','extra_context': {'next': '/discover'}}, name='login'),
    url(r'^logout$', views.logout_user, name='logout'),
    
    url(r'^discover$', views.discover, name='discover'),
    
    url(r'^workouts/manual$', views.manual_workout, name='manual'),
    
    # ex: /polls/5/
    #url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)