from django.forms import ModelForm, TextInput, Textarea
from MainApp.models import Snippet


class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        # Описываем поля, которые будем заполнять в форме
        fields = ['name', 'lang', 'code', 'rate']
       # exclude = ['id']

#  настроить форму
# https://django.fun/tutorials/usovershenstvovannoe-otobrazhenie-form-bootstrap-4-s-pomoshyu-django-crispy-forms/
#