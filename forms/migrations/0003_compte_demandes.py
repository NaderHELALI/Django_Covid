# Generated by Django 3.0.5 on 2020-05-15 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_auto_20200514_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='compte',
            name='demandes',
            field=models.ManyToManyField(to='forms.Demande'),
        ),
    ]
