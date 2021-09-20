from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Section, Job, Item, Method, Procedure




class UserAddForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
                'username', 
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

class CreateSectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ("section_name",)


class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ("job_name",)


class CreateItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("item_name", "purpose", "success", )


class CreateMethodForm(forms.ModelForm):
    class Meta:
        model = Method
        fields = ("method_name", )


class CreateProcedureForm(forms.ModelForm):
    class Meta:
        model = Procedure
        fields = ("procedure_name", )



