from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.edit import CreateView
from django.forms import ModelForm
from django import forms
from django.core.urlresolvers import reverse_lazy

from twitchly.models import BetaInvite

def index(request):    
    return HttpResponse(render_to_response('twitchly/index.html',{},context_instance=RequestContext(request)) )

def invite_thanks(request):
    return HttpResponse(render_to_response('twitchly/betainvite_success.html',{},context_instance=RequestContext(request)) )
    
class BetaInviteForm(ModelForm):
    class Meta:
        model = BetaInvite
        fields = ['email']
    
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