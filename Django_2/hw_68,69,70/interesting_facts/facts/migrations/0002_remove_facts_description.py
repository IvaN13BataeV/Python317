# Generated by Django 5.0.6 on 2024-06-24 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facts',
            name='description',
        ),
    ]
