from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.shortcuts import render_to_response,render
from django.template import RequestContext
from django.views.generic.edit import CreateView

from django.core.urlresolvers import reverse_lazy,reverse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from twitchly.forms import BetaInviteForm,ManualWorkoutForm
from twitchly.models import BetaInvite
from twitchly.models import Workout

from datetime import datetime
from django.utils.timezone import utc

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('twitchly:index'))
    
def index(request):    
    
    return HttpResponse(render_to_response('twitchly/index.html',{},context_instance=RequestContext(request)) )

@login_required(login_url='/login/')
def discover(request):    
    return HttpResponse(render_to_response('twitchly/discover.html',{},context_instance=RequestContext(request)) )
    

def invite_thanks(request):
    return HttpResponse(render_to_response('twitchly/betainvite_success.html',{},context_instance=RequestContext(request)) )
    
         
class BetaInviteCreate(CreateView):
    model = BetaInvite
    fields = ['email']
    form_class = BetaInviteForm
    success_url=reverse_lazy('twitchly:invite_thanks')
    
def manual_workout(request):
    if request.method == 'POST':
        form = ManualWorkoutForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            #Create model and save it        
            workout = Workout()
            workout.name = cd['name']
            workout.type = cd['type']
            
            if( cd['distance'] is not None ):
                workout.distance = cd['distance']
                        
            dur_hh = cd['duration_hh']
            if( dur_hh is None ):
                dur_hh = 0
            
            dur_mm = cd['duration_mm']
            if( dur_mm is None ):
                dur_mm = 0
                
            dur_ss = cd['duration_ss']
            if( dur_ss is None ):
                dur_ss = 0
                
            workout.duration = dur_ss + (dur_mm * 60) + (dur_hh * 3600 )
                
            
            workout_date = cd['workout_date']
            
            date_str = str(workout_date) + " " + str(cd['workout_date_hh']) + ":" + str(cd['workout_date_mm']) + " " + cd['workout_date_ampm']   
            date = datetime.strptime(date_str,"%Y-%m-%d %I:%M %p")
            date = date.replace(tzinfo=utc)       
                 
            workout.workout_date = date
            
            workout.user = request.user
                
            workout.save()
            
            return HttpResponseRedirect(reverse('twitchly:discover'))
        else:
            #Invalid form
            return render(request, 'twitchly/workouts/manual.html', {'form': form})
    else:
        form = ManualWorkoutForm()
        return render(request, 'twitchly/workouts/manual.html', {'form': form})