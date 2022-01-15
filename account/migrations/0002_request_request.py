# Generated by Django 3.2.6 on 2022-01-09 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='request',
            field=models.CharField(blank=True, choices=[('laptop', 'laptop'), ('book', 'book'), ('notes', 'notes'), ('pen', 'pen'), ('cash', 'cash'), ('uniform', 'uniform'), ('speaker', 'speaker')], default='cash', max_length=50, null=True),
        ),
    ]