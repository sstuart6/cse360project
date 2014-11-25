from django import forms

#from .models import SignUp

from .models import User
from .models import Picture
from .models import Settings
#from .models import 

#this is the set up of the user info 
class UserForm(forms.ModelForm) :
    class Meta:
        model = User
        
#setup of the login form
class LoginForm(forms.ModelForm) :
    class Meta:
        model = User
        fields = ['email', 'password']
#setup for 
class PictureForm(forms.ModelForm) :
    photo = forms.FileField(
        label='Select a file',
        help_text='max. 42 MB'
    )
    class Meta:
        model = Picture
        fields = [ 'photo']


class SettingsForm(forms.ModelForm) :
    profile_pic = forms.FileField(
        label='Select a file',
        help_text='max. 42 MB'
    )
    class Meta:
        model = Settings
        fields = [ 'profile_pic']

