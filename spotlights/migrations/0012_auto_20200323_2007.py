# Generated by Django 2.2.11 on 2020-03-23 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotlights', '0011_remove_news_supersede'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='editorial',
        ),
        migrations.AddField(
            model_name='news',
            name='editorials',
            field=models.ManyToManyField(to='spotlights.Editorial'),
        ),
    ]
