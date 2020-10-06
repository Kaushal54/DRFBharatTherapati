# Generated by Django 2.2.4 on 2020-08-25 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_name', models.CharField(blank=True, max_length=255, null=True)),
                ('operating_air_line', models.CharField(blank=True, max_length=255, null=True)),
                ('departure_city', models.CharField(blank=True, max_length=255, null=True)),
                ('arrival_city', models.CharField(blank=True, max_length=255, null=True)),
                ('deate_departure', models.DateField()),
                ('estimated_departure_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Passanger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='flightApp.Flight')),
                ('passanger', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='flightApp.Passanger')),
            ],
        ),
    ]
