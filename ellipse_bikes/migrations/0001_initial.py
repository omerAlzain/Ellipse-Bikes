# Generated by Django 5.0.4 on 2024-05-01 15:26
import django.db.models.deletion
from django.db import migrations
from django.contrib.gis.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('commercial_name', models.CharField(blank=True, max_length=200, null=True)),
                ('country_code', models.CharField(blank=True, max_length=4, null=True)),
                ('cities', models.ManyToManyField(blank=True, to='ellipse_bikes.city')),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Station Number')),
                ('contract', models.ForeignKey(blank=True, null=True,
                                               on_delete=django.db.models.deletion.CASCADE,
                                               to='ellipse_bikes.contract')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('address', models.CharField(max_length=200)),
                ('position', models.PointField()),
                ('shape', models.CharField(max_length=200, null=True, blank=True)),
                ('overflow', models.BooleanField()),
                ('banking', models.BooleanField()),
                ('bonus', models.BooleanField()),

                ('status', models.CharField(max_length=8)),
                ('last_update', models.DateTimeField()),
                ('connected', models.BooleanField()),

                ('total_available_bikes', models.IntegerField()),
                ('total_available_stands', models.IntegerField()),
                ('total_available_mechanical_bikes', models.IntegerField()),
                ('total_available_electrical_bikes', models.IntegerField()),
                ('total_available_electrical_internal_battery_bikes', models.IntegerField()),
                ('total_available_electrical_removable_battery_bikes', models.IntegerField()),
                ('total_capacity', models.IntegerField()),

                ('main_available_bikes', models.IntegerField()),
                ('main_available_stands', models.IntegerField()),
                ('main_available_mechanical_bikes', models.IntegerField()),
                ('main_available_electrical_bikes', models.IntegerField()),
                ('main_available_electrical_internal_battery_bikes', models.IntegerField()),
                ('main_available_electrical_removable_battery_bikes', models.IntegerField()),
                ('main_capacity', models.IntegerField()),

                ('overflow_available_bikes', models.IntegerField(null=True)),
                ('overflow_available_stands', models.IntegerField(null=True)),
                ('overflow_available_mechanical_bikes', models.IntegerField(null=True)),
                ('overflow_available_electrical_bikes', models.IntegerField(null=True)),
                ('overflow_available_electrical_internal_battery_bikes', models.IntegerField(null=True)),
                ('overflow_available_electrical_removable_battery_bikes', models.IntegerField(null=True)),
                ('overflow_capacity', models.IntegerField(null=True)),

                ('last_schedule_run', models.DateTimeField()),
            ],
        ),
    ]
