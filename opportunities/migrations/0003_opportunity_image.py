# Generated by Django 4.2.4 on 2023-08-20 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0002_opportunity_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='image',
            field=models.ImageField(blank=True, upload_to='opportunities'),
        ),
    ]
