# Generated by Django 4.1.3 on 2023-01-18 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_rename_category_categories_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(db_index=True, default='category', max_length=20, verbose_name='name'),
        ),
    ]