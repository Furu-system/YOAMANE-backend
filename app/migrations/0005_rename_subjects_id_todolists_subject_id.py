# Generated by Django 3.2.5 on 2021-09-15 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210914_0218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolists',
            old_name='subjects_id',
            new_name='subject_id',
        ),
    ]