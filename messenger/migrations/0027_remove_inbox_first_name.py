# Generated by Django 2.0.5 on 2018-06-11 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0026_inbox_first_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inbox',
            name='first_name',
        ),
    ]
