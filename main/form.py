from django import forms
from django.db.models.fields import CharField
from .models import SignUpOwnData
from dataclasses import field, fields
from main.models import PgDetailData
from django.utils.log import RequireDebugFalse
class Login(forms.Form):
    email=forms.EmailField(max_length=200)
    password=forms.CharField(max_length=200,widget=forms.PasswordInput)
    
class LoginOwn(forms.Form):
    email=forms.EmailField(max_length=200)
    password=forms.CharField(max_length=200,widget=forms.PasswordInput)
    
class SignUp(forms.Form):
    name=forms.CharField(label="Enter Your name",max_length=200)
    contact=forms.CharField(label="Enter Contact Number",max_length=200)
    email=forms.EmailField(label="Enter Email Address",max_length=200)
    password=forms.CharField(label="Select a Password",max_length=200,widget=forms.PasswordInput)
    
class SignUpOwnForm(forms.Form):
    ownername=forms.CharField(label="Name",max_length=50)
    owneremail=forms.EmailField(label="Email ID",max_length=50)
    ownerpassword=forms.CharField(label="Password",max_length=50,widget=forms.PasswordInput)
    ownercontact=forms.CharField(label="Contact",max_length=50)
    
class PgDetails(forms.ModelForm):
    class Meta:
        model = PgDetailData
        fields = "__all__"
        