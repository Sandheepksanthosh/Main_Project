# Generated by Django 4.2.5 on 2023-11-01 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VehicleName', models.CharField(blank=True, max_length=100, null=True)),
                ('VehicleType', models.CharField(blank=True, max_length=100, null=True)),
                ('VehicleCategory', models.CharField(blank=True, max_length=100, null=True)),
                ('VehiclePrice', models.CharField(blank=True, max_length=100, null=True)),
                ('VehicleImage', models.ImageField(blank=True, null=True, upload_to='Profile')),
            ],
        ),
    ]
