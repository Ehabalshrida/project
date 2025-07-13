from django import forms;
from django.core.validators import MinValueValidator, MaxValueValidator
from . import models
# - This is a simple form class that is used to create a form for user input
class UserForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter first name', 'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter last name'}),label='Last Name', max_length=100, required=True)
    age = forms.IntegerField(label='Age', min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter age'}))
    number = forms.IntegerField(min_value=0, validators=[
            MinValueValidator(0),
            MaxValueValidator(9999999999)
        ], widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter number'}))
# This is a ModelForm class that is used to create a form based on the User model
class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.User
        # Specify the fields to include in the form way one use all fields 
        fields = '__all__'
        # Alternatively, specify individual fields way two
        # fields = ['first_name', 'last_name', 'age', 'number']
        # If you want to exclude certain fields, you can use the exclude option
        # exclude = ['id']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter first name', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter last name', 'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Enter age', 'class': 'form-control'}),
            'number': forms.NumberInput(attrs={'placeholder': 'Enter number', 'class': 'form-control'})
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'age': 'Age',
            'number': 'Number'
        }
        error_messages = {
            'first_name': {
                'required': 'First name is required',
                'max_length': 'First name cannot exceed 100 characters'
            },
            'last_name': {
                'required': 'Last name is required',
                'max_length': 'Last name cannot exceed 100 characters'
            },
            'age': {
                'min_value': 'Age must be a positive number'
            },
            'number': {
                'min_value': 'Number must be a positive number',
                'max_value': 'Number cannot exceed 9999999999'
            }
        }