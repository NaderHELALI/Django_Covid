# Generated by Django 3.0.5 on 2020-05-15 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0005_auto_20200515_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demande',
            name='type',
            field=models.CharField(choices=[('Nourriture', 'Nourriture'), ('Hygiène', 'Hygiène'), ('Nettoyage', 'Nettoyage')], default='Nourriture', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('Nourriture', 'Nourriture'), ('Hygiène', 'Hygiène'), ('Nettoyage', 'Nettoyage')], default='Nourriture', max_length=200),
        ),
    ]