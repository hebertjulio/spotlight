# Generated by Django 2.2.11 on 2020-03-21 18:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotlights', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='editorial',
            options={'verbose_name': 'editorial', 'verbose_name_plural': 'editorials'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'news', 'verbose_name_plural': 'news'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'verbose_name': 'section', 'verbose_name_plural': 'sections'},
        ),
        migrations.AlterModelOptions(
            name='site',
            options={'verbose_name': 'site', 'verbose_name_plural': 'sites'},
        ),
        migrations.AlterField(
            model_name='section',
            name='slots',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='slots'),
        ),
    ]