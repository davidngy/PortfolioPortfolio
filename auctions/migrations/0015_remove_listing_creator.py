# Generated by Django 4.2.7 on 2023-12-14 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_listing_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='creator',
        ),
    ]