# Generated by Django 4.1.3 on 2023-01-04 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0005_carts_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='carts',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='created at'),
        ),
        migrations.AddField(
            model_name='carts',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='updated at'),
        ),
    ]
