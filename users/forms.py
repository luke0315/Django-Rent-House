from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django import forms
 
 
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', )
 
class CustomUserChangeForm(UserChangeForm):
    password = None
 
    class Meta:
        model = CustomUser
        fields = ['username','email', 'first_name', 'last_name', 'dob', 'location' ]
        widgets = { 'dob': DatePickerInput() }
 
