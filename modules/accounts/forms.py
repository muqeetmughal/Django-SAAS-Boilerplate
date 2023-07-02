from django import forms
from django.contrib.auth import get_user_model

UserAccountModel= get_user_model()

class UserAccountForm(forms.ModelForm):
    class Meta:
        model = UserAccountModel
        fields = ['name', 'email', 'phone_number']
