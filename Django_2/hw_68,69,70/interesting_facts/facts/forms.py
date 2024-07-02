from django.forms import ModelForm
from .models import Facts


class FactsForm(ModelForm):
    class Meta:
        model = Facts
        fields = ['title', 'description', 'image']
