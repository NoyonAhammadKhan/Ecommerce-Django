from django.forms import ModelForm
from App_Login.models import UserProfile, Profile
from django.contrib.auth.forms import UserCreationForm

#forms for user

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude =('user',)

class SignupForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ('email', 'password1','password2')

