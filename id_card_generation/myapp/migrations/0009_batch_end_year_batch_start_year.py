# Generated by Django 5.1.1 on 2024-10-23 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_remove_batch_end_year_remove_batch_start_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='end_year',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='batch',
            name='start_year',
            field=models.PositiveIntegerField(null=True),
        ),
    ]