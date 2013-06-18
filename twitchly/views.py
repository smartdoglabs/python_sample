from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.edit import CreateView
from django.forms import ModelForm
from django import forms
from django.core.urlresolvers import reverse_lazy,reverse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from twitchly.models import BetaInvite

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
    
class BetaInviteForm(ModelForm):
    class Meta:
        model = BetaInvite
        fields = ['email']
    
    def __init__(self, *args, **kwargs):            
        super(BetaInviteForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = u'Email'
        self.fields['email'].widget.attrs['autofocus'] = u'autofocus'
        
        
    def clean(self):
        cleaned_data = super(BetaInviteForm,self).clean()
        
        if( 'email' in cleaned_data ):
            email_addr = cleaned_data['email']
        
            invited = BetaInvite.objects.filter(email=email_addr)
        
            if( invited.exists() ):
                raise forms.ValidationError("Settle down! We already have your invite request. Tell your friends!")

        return cleaned_data
        
    
class BetaInviteCreate(CreateView):
    model = BetaInvite
    fields = ['email']
    form_class = BetaInviteForm
    success_url=reverse_lazy('twitchly:invite_thanks')