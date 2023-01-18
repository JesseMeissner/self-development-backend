# Generated by Django 4.1.3 on 2023-01-18 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_alter_categories_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='name',
        ),
        migrations.AddField(
            model_name='categories',
            name='category',
            field=models.CharField(db_index=True, default='category', max_length=20, verbose_name='category'),
        ),
    ]