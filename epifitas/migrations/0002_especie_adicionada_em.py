# Generated by Django 3.2.5 on 2021-08-11 15:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('epifitas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='especie',
            name='adicionada_em',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
