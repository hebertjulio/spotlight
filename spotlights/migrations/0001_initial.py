# Generated by Django 2.2.11 on 2020-03-25 11:07

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('slug', models.SlugField(max_length=100, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'editorial',
                'verbose_name_plural': 'editorials',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('slug', models.SlugField(max_length=100, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'page',
                'verbose_name_plural': 'pages',
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='slug')),
                ('url', models.URLField(unique=True, verbose_name='url')),
            ],
            options={
                'verbose_name': 'site',
                'verbose_name_plural': 'sites',
            },
        ),
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('slug', models.SlugField(max_length=100, verbose_name='slug')),
                ('slots', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='slots')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spotlights.Page')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spotlights.Site')),
            ],
            options={
                'verbose_name': 'panel',
                'verbose_name_plural': 'panels',
                'unique_together': {('page', 'slug')},
            },
        ),
        migrations.AddField(
            model_name='page',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spotlights.Site'),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('headline', models.CharField(max_length=100, verbose_name='headline')),
                ('blurb', models.CharField(blank=True, max_length=100, verbose_name='blurb')),
                ('url', models.URLField(verbose_name='url')),
                ('image', models.ImageField(blank=True, upload_to='news', verbose_name='image')),
                ('editorials', models.ManyToManyField(to='spotlights.Editorial')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spotlights.Site')),
            ],
            options={
                'verbose_name': 'news',
                'verbose_name_plural': 'news',
                'ordering': ['-created'],
                'unique_together': {('site', 'url')},
            },
        ),
        migrations.CreateModel(
            name='Layout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('slug', models.SlugField(max_length=100, verbose_name='slug')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spotlights.Page')),
                ('panel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spotlights.Panel')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spotlights.Site')),
            ],
            options={
                'verbose_name': 'layout',
                'verbose_name_plural': 'layouts',
                'unique_together': {('panel', 'slug')},
            },
        ),
        migrations.AddField(
            model_name='editorial',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spotlights.Site'),
        ),
        migrations.CreateModel(
            name='RelatedNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('headline', models.CharField(max_length=100, verbose_name='headline')),
                ('url', models.URLField(verbose_name='url')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spotlights.News')),
            ],
            options={
                'verbose_name': 'related news',
                'verbose_name_plural': 'related news',
                'unique_together': {('news', 'url')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='page',
            unique_together={('site', 'slug')},
        ),
        migrations.CreateModel(
            name='NewsPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('layout', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='spotlights.Layout')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spotlights.News')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spotlights.Page')),
                ('panel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='spotlights.Panel')),
            ],
            options={
                'verbose_name': 'news page',
                'verbose_name_plural': 'news pages',
                'unique_together': {('news', 'page')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='editorial',
            unique_together={('site', 'slug')},
        ),
    ]
