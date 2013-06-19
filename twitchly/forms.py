from django.forms import ModelForm
from django import forms
from django.utils import timezone
from twitchly.models import BetaInvite


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

class ManualWorkoutForm(forms.Form):
    name = forms.CharField(required=True)
    type = forms.ChoiceField(widget = forms.Select(), choices = ([("swim", "Swim"), ("bike", "Bike"), ("run", "Run"), ("walk", "Walk"),]) )
    distance = forms.FloatField(required=False,min_value=0.0)
    workout_date = forms.DateField(required=True,initial=timezone.now(),widget=forms.DateInput(format = '%m/%d/%Y'), input_formats=('%m/%d/%Y',))
    workout_date_hh = forms.IntegerField(required=True,min_value=0,max_value=12)
    workout_date_mm = forms.IntegerField(required=True,min_value=0,max_value=59)
    workout_date_ampm = forms.ChoiceField(widget = forms.Select(), choices = ([("am", "AM"), ("pm", "PM"),]) )
    duration_hh = forms.IntegerField(required=False,min_value=0)
    duration_mm = forms.IntegerField(required=False,min_value=0,max_value=59)
    duration_ss = forms.IntegerField(required=False,min_value=0,max_value=59)
    
    def __init__(self, *args, **kwargs):            
        super(forms.Form, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = u'Name'
        self.fields['workout_date_hh'].widget.attrs['placeholder'] = u'hh'
        self.fields['workout_date_mm'].widget.attrs['placeholder'] = u'mm'
        self.fields['duration_hh'].widget.attrs['placeholder'] = u'hh'
        self.fields['duration_mm'].widget.attrs['placeholder'] = u'mm'
        self.fields['duration_ss'].widget.attrs['placeholder'] = u'ss'
        self.fields['name'].widget.attrs['autofocus'] = u'autofocus'
    
    