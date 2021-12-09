from django.forms import ModelForm, TextInput, Textarea
from MainApp.models import Snippet
from django.forms import TextInput, Textarea


class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        # Описываем поля, которые будем заполнять в форме
        fields = ['id', 'name', 'lang', 'code', 'rate']
        labels = {
            "name": "",
            "lang": "",
        }
        widgets = {
            "name": TextInput(attrs = {"placeholder": "Название виджета", "class": "name"}),
            # "lang": TextInput(attrs = {"placeholder": "Язык программирования"})
        }
       # exclude = []

#  настроить форму
# https://django.fun/tutorials/usovershenstvovannoe-otobrazhenie-form-bootstrap-4-s-pomoshyu-django-crispy-forms/
#