# Generated by Django 4.1.2 on 2022-10-19 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0007_alter_shipment_delivery_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shipment',
            old_name='country_recipient',
            new_name='delivery_country',
        ),
        migrations.RemoveField(
            model_name='shipment',
            name='company_owner',
        ),
        migrations.RemoveField(
            model_name='shipment',
            name='company_sender',
        ),
        migrations.RemoveField(
            model_name='shipment',
            name='country_sender',
        ),
        migrations.AddField(
            model_name='shipment',
            name='company',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='companies', to='shipments.company'),
            preserve_default=False,
        ),
    ]
