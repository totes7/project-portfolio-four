# Generated by Django 3.2.18 on 2023-03-27 13:56

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
                ('capacity', models.IntegerField(default=2)),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('date', models.DateField(default=datetime.date.today)),
                ('time', models.IntegerField(choices=[(1, '12:00 - 14:00'), (2, '14:00 - 16:00'), (3, '18:00 - 20:00'), (4, '20:00 - 22:00')], default=1)),
                ('guests', models.IntegerField(default=1)),
                ('special_request', models.TextField(blank=True, max_length=200)),
                ('updated', models.BooleanField(default=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_customer', to=settings.AUTH_USER_MODEL)),
                ('table_number', models.ManyToManyField(related_name='booked_table', to='booking.Table')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
