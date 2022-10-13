# Generated by Django 4.1.2 on 2022-10-13 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mantenimientos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kilometraje', models.PositiveIntegerField(verbose_name='Kilometraje')),
                ('descripcion', models.CharField(max_length=7, verbose_name='Descripcion')),
                ('costo', models.PositiveIntegerField(verbose_name='Costo')),
                ('fecha', models.DateTimeField(verbose_name='Fecha')),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autos.autos')),
            ],
            options={
                'verbose_name': 'mantenimiento',
                'verbose_name_plural': 'Mantenimientos',
            },
        ),
    ]
