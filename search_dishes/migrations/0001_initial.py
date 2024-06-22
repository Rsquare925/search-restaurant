# Generated by Django 5.0.6 on 2024-06-21 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('items', models.JSONField()),
                ('lat_long', models.CharField(max_length=255)),
                ('full_details', models.JSONField()),
            ],
        ),
    ]
