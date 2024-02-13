from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import Group
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div, HTML

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
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    remember_me = forms.BooleanField(label='Remember me', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'register_login:login'
        self.helper.layout = Layout(
            'email',
            'password',
            'remember_me',
            Div(
                Submit('submit', 'Login', css_class='btn btn-primary btn-block mx-4 my-2'),
                HTML('<a href="{% url "register_login:sso_login" %}" class="btn btn-outline-dark mx-4 my-2">\
                     Or login with SSO</a>'),
                css_class='d-grid',
            )    
        )


class RegisterForm(forms.ModelForm):
    password_confirm = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'register_login:register'
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'email',
            'password',
            'password_confirm',
            Div(
                Submit('submit', 'Create Account', css_class='btn btn-primary btn-block'),
                css_class='d-grid',
            )    
        )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")
