# Generated by Django 4.1.3 on 2023-01-04 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_alter_item_clicked'),
        ('carts', '0003_carts_cart_ids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carts',
            name='cart_ids',
        ),
        migrations.RemoveField(
            model_name='carts',
            name='subtotal',
        ),
        migrations.AddField(
            model_name='carts',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='items.item'),
        ),
    ]
