# Generated by Django 3.1.5 on 2021-02-20 03:58

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0021_auto_20210220_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='long_description',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Полное описание'),
        ),
        migrations.AlterField(
            model_name='location',
            name='short_description',
            field=models.TextField(blank=True, verbose_name='Краткое описание'),
        ),
    ]