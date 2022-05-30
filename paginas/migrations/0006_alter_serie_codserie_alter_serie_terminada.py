# Generated by Django 4.0.4 on 2022-05-27 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0005_serie_codserie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serie',
            name='codserie',
            field=models.CharField(blank=True, default=None, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='serie',
            name='terminada',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
