# Generated by Django 3.2.5 on 2021-08-11 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('epifitas', '0002_especie_adicionada_em'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='especie',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='epifitas.especie'),
        ),
        migrations.AlterField(
            model_name='infogeografica',
            name='especie',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='epifitas.especie'),
        ),
        migrations.AlterField(
            model_name='inforeproducao',
            name='especie',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='epifitas.especie'),
        ),
    ]
