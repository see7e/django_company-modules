from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, HTML
from crispy_forms.bootstrap import Div
from .models import Task

class BaseTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

        name = forms.CharField(max_length=100)
        description = forms.CharField(widget=forms.Textarea)
        start_date = forms.DateTimeField()
        due_date = forms.DateTimeField()

    def __init__(self, *args, creator, type, **kwargs):
        super().__init__(*args, **kwargs)
        self.creator = creator
        self.type = type
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_class = 'modal-content'
        self.helper.layout = self.build()

    def save(self, *args, **kwargs):
        self.instance.created_by = self.creator
        return super().save(*args, **kwargs)
    
    def build(self):
        return Layout(
            Div(
                'name',
                'description',
                'start_date',
                'due_date',
                ButtonHolder(
                    HTML('<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>'),
                    HTML('<button type="submit" class="btn btn-primary">Create</button>'),
                ),
                css_class='modal-body'
            )
        )