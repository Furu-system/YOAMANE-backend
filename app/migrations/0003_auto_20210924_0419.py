# Generated by Django 3.2.5 on 2021-09-24 04:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_todolists_estimated_work_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignments',
            name='collaborating_group_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignment_group_id', to='app.grouptags'),
        ),
        migrations.AlterField(
            model_name='assignments',
            name='collaborating_member_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignment_member_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='schedules',
            name='collaborating_group_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedule_group_id', to='app.grouptags'),
        ),
        migrations.AlterField(
            model_name='schedules',
            name='collaborating_member_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedule_member_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='todolists',
            name='collaborating_group_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='todolist_group_id', to='app.grouptags'),
        ),
        migrations.AlterField(
            model_name='todolists',
            name='collaborating_member_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='todolist_member_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
