from django.db import models
from django.contrib.auth.models import User

LANG_CHOICES = (
    ('', 'Выбор языка'),
    ("py", "python"),
    ("js", "javaScript"),
    ("cs", "C#"),
)

class Snippet(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=30, choices=LANG_CHOICES)
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    rate = models.PositiveSmallIntegerField(null=False, blank=True, default=1)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
    public = models.BooleanField(default=True) # true - public, false - private

    def __str_(self):
        return self.__repr__()

    def __repr__(self):
        return f"{self.name} ({self.lang}) user:{self.user}"

class Comment(models.Model):
    text = models.TextField(max_length=2000)
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
    snippet = models.ForeignKey(to=Snippet, on_delete=models.CASCADE, related_name="comments")