from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, HTML
from crispy_forms.bootstrap import Div
from core.forms import BaseTaskForm
from .models import Item

from django_select2 import forms as s2forms


class ItemSelect2Widget(s2forms.ModelSelect2Widget):
    search_fields = [
        "name__icontains",
    ]


# class OutboundRequestForm(forms.ModelForm):
#     item = forms.ModelChoiceField(queryset=Item.objects.all())

#     class Meta:
#         model = OutboundRequest
#         fields = ['item', 'name', 'email', 'message', 'address', 'phone']

#     def __init__(self, *args, **kwargs)e
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper(self)
#         self.helper.form_method = 'post'
#         self.helper.form_class = 'modal-content'
#         self.helper.layout = self.build()

#     def build(self):
#         return Layout(
#             Div(
#                 'item',
#                 'name',
#                 'email',
#                 'message',
#                 'address',
#                 'phone',
#                 ButtonHolder(
#                     HTML('<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>'),
#                     HTML('<button type="submit" class="btn btn-primary">Send message</button>'),
#                 ),
#                 css_class='modal-body'
#             )
#         )


class OrderForm(BaseTaskForm):
    # task object (name, description, user, type, status, start_date, due_date, created_at, created_by, updated_at, updated_by)
    # outboundrequest object (license_plate, products(outboundproduct), task, destination_code)
    license_plate = forms.CharField(max_length=100)
    products = forms.ModelMultipleChoiceField(
        queryset=Item.objects.all(),
        # widget=forms.CheckboxSelectMultiple,
        widget=ItemSelect2Widget,
        help_text="Select from the available products to be shipped.",
    )

    destination_code = forms.CharField(max_length=100)

    def __init__(self, *args, creator, **kwargs):
        super().__init__(*args, creator=creator, type="order", **kwargs)

    def build(self):
        return Layout(
            Div(
                "name",
                "description",
                "license_plate",
                "products",
                "destination_code",
                "start_date",
                "due_date",
                ButtonHolder(
                    HTML(
                        '<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>'
                    ),
                    HTML(
                        '<button type="submit" class="btn btn-primary">Create</button>'
                    ),
                ),
                css_class="modal-body",
            )
        )
