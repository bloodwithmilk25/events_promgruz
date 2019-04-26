# Generated by Django 2.0.9 on 2018-11-29 13:02

import django.core.validators
from django.db import migrations, models
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20181122_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='new_tab',
            field=models.BooleanField(default=False, verbose_name='Открывать сайт конференции в новой вкладке'),
        ),
        migrations.AlterField(
            model_name='location',
            name='address',
            field=django_google_maps.fields.AddressField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='location',
            name='country',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='location',
            name='geolocation',
            field=django_google_maps.fields.GeoLocationField(blank=True, help_text='XX.XXX ,YY.YYYY', max_length=100),
        ),
        migrations.AlterField(
            model_name='location',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]