# Generated by Django 5.1.1 on 2024-10-27 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_remove_batch_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
