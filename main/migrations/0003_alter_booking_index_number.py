# Generated by Django 4.2.11 on 2024-04-28 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='index_number',
            field=models.IntegerField(),
        ),
    ]