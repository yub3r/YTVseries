# Generated by Django 4.0.4 on 2022-05-04 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0002_serie_codserie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serie',
            name='codserie',
            field=models.CharField(default='NameS01', max_length=25),
        ),
    ]
