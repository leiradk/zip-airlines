# Generated by Django 3.0.7 on 2020-06-26 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airplane',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airplane_id', models.IntegerField()),
                ('fuel_tank', models.IntegerField()),
                ('consumption_per_minute', models.FloatField()),
            ],
        ),
    ]
