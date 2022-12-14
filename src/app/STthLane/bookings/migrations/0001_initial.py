# Generated by Django 4.1.1 on 2022-09-14 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lanes',
            fields=[
                ('lane_nr', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booker_phone', models.CharField(default='No phone', max_length=13)),
                ('start_time', models.DateTimeField(null=True)),
                ('end_date', models.DateTimeField(null=True)),
                ('payed', models.BooleanField(default=False)),
                ('lane_nr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.lanes')),
            ],
        ),
    ]
