# Generated by Django 2.2.11 on 2020-03-23 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotlights', '0014_auto_20200323_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='editorials',
            field=models.ManyToManyField(blank=True, to='spotlights.Editorial'),
        ),
    ]