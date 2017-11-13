from django import forms

from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'type':'password','placeholder':'Password','id':'p' }))
    confirmpassword = forms.CharField(widget=forms.PasswordInput(attrs={'type':'password','placeholder':'Confirm Password','id':'cp'}))
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-inline','type':'text','placeholder':'First name'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-inline','type':'text','placeholder':'Last name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'type':'text','placeholder':'Username','id':'id_username'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'type':'text','placeholder':'Email'}))
    class Meta:
        model = User
        fields = ['firstname' , 'lastname','username', 'email', 'password' ,'confirmpassword'  ]