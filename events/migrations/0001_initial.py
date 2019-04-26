# Generated by Django 2.0.9 on 2018-11-06 14:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_google_maps.fields
import events.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('slug', models.SlugField(max_length=35)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=35)),
                ('description', models.TextField(blank=True)),
                ('web_site', models.URLField(blank=True)),
                ('year', models.IntegerField(blank=True, choices=[(2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021)], default=2018, verbose_name='year')),
                ('logo', models.ImageField(blank=True, upload_to=events.models.image_name)),
                ('banner', models.ImageField(blank=True, upload_to=events.models.image_name)),
                ('date_start', models.DateTimeField(blank=True, null=True)),
                ('date_end', models.DateTimeField(blank=True, null=True)),
                ('published', models.BooleanField(default=False)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='events', to='events.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.ImageField(upload_to=events.models.image_name)),
                ('order', models.DecimalField(blank=True, decimal_places=2, help_text='Указать если нужно задать свой порядок картинкам', max_digits=5, null=True)),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='events.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to=events.models.image_name)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('address', django_google_maps.fields.AddressField(max_length=200)),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$')])),
                ('web_site', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('slug', models.SlugField(max_length=35)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='events.Location'),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='events.Location'),
        ),
        migrations.AddField(
            model_name='event',
            name='parent_event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='events.Event'),
        ),
        migrations.AddField(
            model_name='event',
            name='related_events',
            field=models.ManyToManyField(blank=True, related_name='_event_related_events_+', to='events.Event'),
        ),
        migrations.AddField(
            model_name='event',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='events', to='events.Tag'),
        ),
    ]
