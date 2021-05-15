from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserAddForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
                'username', 
                'email', 
                'last_name',
                'first_name',
                'password1', 
                'password2'
                ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
