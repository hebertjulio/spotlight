# Generated by Django 2.2.11 on 2020-03-22 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotlights', '0009_relatednews'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='sites',
            field=models.ManyToManyField(to='spotlights.Site'),
        ),
    ]
