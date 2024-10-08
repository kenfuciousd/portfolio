# Generated by Django 5.0.6 on 2024-07-15 17:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydjangoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('package_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('weight', models.FloatField()),
                ('dimensions', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('in_transit', 'In Transit'), ('delivered', 'Delivered')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=15)),
                ('role', models.CharField(choices=[('courier', 'Courier'), ('client', 'Client')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('delivery_id', models.AutoField(primary_key=True, serialize=False)),
                ('pickup_location', models.CharField(max_length=200)),
                ('dropoff_location', models.CharField(max_length=200)),
                ('delivery_status', models.CharField(choices=[('pending', 'Pending'), ('in_transit', 'In Transit'), ('delivered', 'Delivered')], max_length=20)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mydjangoapp.package')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_deliveries', to='mydjangoapp.user')),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courier_deliveries', to='mydjangoapp.user')),
            ],
        ),
    ]
