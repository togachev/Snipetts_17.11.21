from django.forms import ModelForm, TextInput, Textarea
from MainApp.models import Snippet
from django.forms import TextInput, Textarea, CharField, PasswordInput, ValidationError
from django.contrib.auth.models import User

class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        # Описываем поля, которые будем заполнять в форме
        fields = ['id', 'name', 'lang', 'code', 'rate', 'public']
        labels = {
            "name": "Сниппет",
            "lang": "Язык",
            "rate": "Рейтинг",
            "code": "Код",
            "public": "Доступ(закрыт/открыт)",
        }
        widgets = {
            "name": TextInput(attrs = {"placeholder": "Введите название сниппета", "class": "name"}),
            # "lang": TextInput(attrs = {"placeholder": "Язык программирования"}),
        }

#  настроить форму
# https://django.fun/tutorials/usovershenstvovannoe-otobrazhenie-form-bootstrap-4-s-pomoshyu-django-crispy-forms/
#

class UserRegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]

    password1 = CharField(label="password", widget=PasswordInput)
    password2 = CharField(label="password confirm", widget=PasswordInput)

    def clean_password2(self):
        pass1 = self.cleaned_data.get("password1")
        pass2 = self.cleaned_data.get("password2")
        if pass1 and pass2 and pass1 == pass2:
            return pass2
        raise ValidationError("Пароли не совпадают или пустые")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user