# Generated by Django 4.1.3 on 2023-01-21 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0015_item_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='likes',
        ),
    ]