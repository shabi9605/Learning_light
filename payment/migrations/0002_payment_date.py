# Generated by Django 3.1.4 on 2021-11-18 08:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]