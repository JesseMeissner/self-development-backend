# Generated by Django 4.1.3 on 2022-12-31 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_alter_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='likes',
            field=models.IntegerField(default=0, verbose_name='likes'),
        ),
    ]
