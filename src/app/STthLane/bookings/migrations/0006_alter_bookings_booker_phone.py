# Generated by Django 4.1.1 on 2022-09-17 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_remove_bookings_lane_nr_bookings_lanes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='booker_phone',
            field=models.CharField(default='xxx-xxxx', max_length=15),
        ),
    ]
