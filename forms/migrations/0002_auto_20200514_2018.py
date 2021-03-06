# Generated by Django 3.0.5 on 2020-05-14 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demande',
            name='date',
        ),
        migrations.RemoveField(
            model_name='demande',
            name='produits',
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.IntegerField(choices=[(1, 'Nourriture'), (2, 'Hygiène'), (3, 'Nettoyage')], null=True),
        ),
        migrations.AlterField(
            model_name='demande',
            name='type',
            field=models.IntegerField(choices=[(1, 'Nourriture'), (2, 'Hygiène'), (3, 'Nettoyage')], default=1),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=2)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='forms.Product')),
            ],
        ),
        migrations.AddField(
            model_name='demande',
            name='items',
            field=models.ManyToManyField(to='forms.Item'),
        ),
    ]
