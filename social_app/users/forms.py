from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    
    
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    password1 = forms.CharField(label='Confirm password',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','email','first_name')
        
    def check_password(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise forms.ValidationError('Passwords do not match!')
        return self.cleaned_data['password2']