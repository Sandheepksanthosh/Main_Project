# Generated by Django 4.2.5 on 2023-11-10 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0006_bikedetailsdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikedetailsdb',
            name='Vehiclename',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bikedetailsdb',
            name='Fueltankcapacity',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bikedetailsdb',
            name='Mileage',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]