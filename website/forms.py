from django.shortcuts import render
from django import forms

class EmailForm(forms.Form):

    email = forms.EmailField()


class CompanyInfoForm(forms.Form):

    name = forms.CharField(max_length=50)
    company_name = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=13)
    company_info = forms.CharField(widget=forms.Textarea)

class OTPVerificationForm(forms.Form):

    otp  = forms.CharField(max_length=6)



class StartTrialForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg'}), required=True)
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    company_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    phone = forms.CharField(max_length=13, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))
