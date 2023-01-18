# Generated by Django 4.1.3 on 2023-01-18 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(db_index=True, default='category', max_length=20, verbose_name='category')),
            ],
            options={
                'db_table': 'categories',
            },
        ),
    ]