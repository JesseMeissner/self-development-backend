# Generated by Django 4.1.3 on 2023-01-06 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0011_alter_item_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(db_index=True, default='item', max_length=30, verbose_name='Name'),
        ),
    ]