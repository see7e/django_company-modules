from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import Group

from .models import CustomUser


# # This form is only used in admin to facilitate the selection of users for a group.
class MultiSelectionGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude = []
    
    users = forms.ModelMultipleChoiceField(
        label=('CustomUsers'),
        queryset=CustomUser.objects.all(), 
        required=False,
        widget=FilteredSelectMultiple('users', False),
    )
    
    
    def __init__(self, *args, **kwargs):
        # Do the normal form initialisation.
        super(MultiSelectionGroupForm, self).__init__(*args, **kwargs)
        # If it is an existing group (saved objects have a pk).
        if self.instance.pk:
            # Populate the users field with the current Group users.
            self.fields['users'].initial = self.instance.user_set.all()
    
    
    def save_m2m(self):
        # Add the users to the Group.
        self.instance.user_set.set(self.cleaned_data['users'])
    
    
    def save(self, *args, **kwargs):
        # Default save
        instance = super(MultiSelectionGroupForm, self).save()
        self.save_m2m() # Save many-to-many data
        return instance
    

class LoginForm(forms.Form):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']

    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    # remember_me = forms.BooleanField(label='Remember me', required=False)

    def build(self, *args, **kwargs):
        self.fields['email'].widget = forms.EmailInput(
            attrs={'class': 'form-control', 'required': True}
        )
        self.fields['password'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'required': True}
        )
        self.fields['remember_me'].widget = forms.CheckboxInput(
            attrs={'class': 'form-check-input'}
        )
        # self.fields['remember_me'].label = 'Remember me'


class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password']
    
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.build_fields()


    def build_fields(self):
        self.fields['email'].widget = forms.EmailInput(
            attrs={'class': 'form-control', 'required': True}
        )
        self.fields['password'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'required': True}
        )
        self.fields['first_name'].widget = forms.TextInput(
            attrs={'class': 'form-control', 'required': True}
        )
        self.fields['last_name'].widget = forms.TextInput(
            attrs={'class': 'form-control', 'required': True}
        )


    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user