# Generated by Django 2.2.4 on 2020-08-02 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('score', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
