from django.forms import ModelForm
from .models import Client


class ClienteModel(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'last_name', 'age', 'salary', 'email', 'photo']




