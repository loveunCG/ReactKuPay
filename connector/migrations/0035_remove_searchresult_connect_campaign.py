# Generated by Django 2.0.5 on 2018-06-14 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connector', '0034_auto_20180605_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searchresult',
            name='connect_campaign',
        ),
    ]