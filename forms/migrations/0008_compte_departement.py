# Generated by Django 2.1.15 on 2020-05-22 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0007_auto_20200515_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='compte',
            name='departement',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
