# Generated by Django 2.2.11 on 2020-03-23 21:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('spotlights', '0013_auto_20200323_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='editorials',
            field=models.ManyToManyField(blank=True, to='spotlights.Editorial'),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('slug', models.SlugField(max_length=100, verbose_name='slug')),
                ('editorials', models.ManyToManyField(blank=True, to='spotlights.Panel')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spotlights.Site')),
            ],
            options={
                'verbose_name': 'page',
                'verbose_name_plural': 'pages',
                'unique_together': {('site', 'slug')},
            },
        ),
    ]