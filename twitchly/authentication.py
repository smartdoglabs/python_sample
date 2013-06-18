from django.contrib.auth.forms import AuthenticationForm

class TwitchlyLoginForm(AuthenticationForm):
    
    def __init__(self, *args, **kwargs):            
        super(TwitchlyLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = u'Username'
        self.fields['username'].widget.attrs['autofocus'] = u'autofocus'
        self.fields['password'].widget.attrs['placeholder'] = u'Password'
        