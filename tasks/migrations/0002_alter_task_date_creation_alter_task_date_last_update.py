# Generated by Django 5.0.6 on 2024-06-26 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_creation',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_last_update',
            field=models.DateField(),
        ),
    ]
