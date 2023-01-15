from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation


class CustomerRegistrationForm(UserCreationForm):    
    password1 = forms.CharField(label='Enter Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs= {'class':'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs= {'class':'form-control', 'required':'required'}))

    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']
        label = { 'email' : 'Email'}
        widgets = { 'username' : forms.TextInput(attrs= {'class':'form-control'})}



class LoginForm(AuthenticationForm):
    username= UsernameField(widget= forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))



class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Old Password",strip=False, widget=forms.PasswordInput(attrs = { 'class': "form-control", 'auto-complete':"current-password", 'auto-focus':True}))
    new_password1 = forms.CharField(label="New Password",strip=False, help_text=password_validation.password_validators_help_text_html(),widget=forms.PasswordInput(attrs = { 'class': "form-control", 'auto-complete':"new-password", 'auto-focus':True}))
    new_password2 = forms.CharField(label="Confirm New Password",strip=False, widget=forms.PasswordInput(attrs = { 'class': "form-control", 'auto-complete':"new-password", 'auto-focus':True}))



class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_('Email'), max_length=200, widget=forms.EmailInput(attrs={'autocomplete':'email', 'class':'form-control'}))


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label="New Password",strip=False, help_text=password_validation.password_validators_help_text_html(),widget=forms.PasswordInput(attrs = { 'class': "form-control", 'auto-complete':"new-password", 'auto-focus':True}))
    new_password2 = forms.CharField(label="Confirm New Password",strip=False, widget=forms.PasswordInput(attrs = { 'class': "form-control", 'auto-complete':"new-password", 'auto-focus':True}))



from .models import Customer

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'lacality','city', 'zipcode','state']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'lacality': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'zipcode': forms.NumberInput(attrs={'class': 'form-control'}),
        }