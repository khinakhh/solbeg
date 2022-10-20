# Generated by Django 4.1.2 on 2022-10-08 14:29

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('country', django_countries.fields.CountryField(default='UK', max_length=2)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('country_sender', django_countries.fields.CountryField(default='UK', max_length=2)),
                ('country_recipient', django_countries.fields.CountryField(default='PL', max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('availability', models.CharField(choices=[('AVAILABLE', 'available'), ('NOT AVAILABLE', 'not available')], default='AVAILABLE', max_length=20)),
                ('delivery_status', models.IntegerField(choices=[(0, 'information received'), (1, 'in queue'), (2, 'in transit'), (3, 'available for pickup'), (4, 'delivered'), (5, 'canceled')], default=0)),
                ('company_owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='company_owner', to='shipments.company')),
                ('company_sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_senders', to='shipments.company')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
