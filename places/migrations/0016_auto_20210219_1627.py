# Generated by Django 3.1.5 on 2021-02-19 13:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0015_auto_20210219_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='lat',
            field=models.FloatField(verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='location',
            name='lng',
            field=models.FloatField(verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='location',
            name='properties_placeId',
            field=models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Уникальный идентификатор локации'),
        ),
    ]