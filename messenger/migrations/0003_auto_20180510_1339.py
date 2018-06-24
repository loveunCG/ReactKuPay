# Generated by Django 2.0.5 on 2018-05-10 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0002_auto_20180508_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='owner',
        ),
        migrations.AddField(
            model_name='inbox',
            name='linkedin_id',
            field=models.CharField(default=1, max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='messenger',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messenger_messages', to='messenger.Campaign'),
        ),
        migrations.AddField(
            model_name='message',
            name='type',
            field=models.CharField(blank=True, choices=[('Replied', 'Replied'), ('Talking', 'Talking'), ('Talking & Replied', 'Talking & Replied'), ('Connect Req', 'Connect Req')], default='Talking', max_length=50),
        ),
    ]