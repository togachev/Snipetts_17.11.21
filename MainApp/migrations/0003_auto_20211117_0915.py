# Generated by Django 3.1 on 2021-11-17 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_auto_20211117_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
