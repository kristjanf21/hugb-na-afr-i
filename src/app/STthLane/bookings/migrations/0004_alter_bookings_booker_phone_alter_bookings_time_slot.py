# Generated by Django 4.1.1 on 2022-09-17 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_alter_bookings_time_slot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='booker_phone',
            field=models.CharField(default='xxx-xxxx', max_length=13),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='time_slot',
            field=models.CharField(default='dd/mm/yyyy', max_length=13),
        ),
    ]