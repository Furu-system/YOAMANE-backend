# Generated by Django 3.2.5 on 2021-09-27 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210924_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedules',
            name='is_class',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
