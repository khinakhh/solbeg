# Generated by Django 4.1.2 on 2022-10-18 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0004_alter_shipment_company_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
