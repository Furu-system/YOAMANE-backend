# Generated by Django 3.2.5 on 2021-09-24 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210924_0422'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignments',
            old_name='collaborating_group_id',
            new_name='collaborating_group',
        ),
        migrations.RenameField(
            model_name='assignments',
            old_name='collaborating_member_id',
            new_name='collaborating_member',
        ),
        migrations.RenameField(
            model_name='assignments',
            old_name='to_do_list_id',
            new_name='to_do_list',
        ),
        migrations.RenameField(
            model_name='assignments',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='friends',
            old_name='friend_user_id',
            new_name='friend_user',
        ),
        migrations.RenameField(
            model_name='friends',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='grouptags',
            old_name='create_user_id',
            new_name='create_user',
        ),
        migrations.RenameField(
            model_name='grouptags',
            old_name='groupname_id',
            new_name='groupname',
        ),
        migrations.RenameField(
            model_name='grouptags',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='schedules',
            old_name='collaborating_group_id',
            new_name='collaborating_group',
        ),
        migrations.RenameField(
            model_name='schedules',
            old_name='collaborating_member_id',
            new_name='collaborating_member',
        ),
        migrations.RenameField(
            model_name='schedules',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='subjects',
            old_name='color_id',
            new_name='color',
        ),
        migrations.RenameField(
            model_name='subjects',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='timetables',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='timetabletimes',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='todolists',
            old_name='collaborating_group_id',
            new_name='collaborating_group',
        ),
        migrations.RenameField(
            model_name='todolists',
            old_name='collaborating_member_id',
            new_name='collaborating_member',
        ),
        migrations.RenameField(
            model_name='todolists',
            old_name='subject_id',
            new_name='subject',
        ),
        migrations.RenameField(
            model_name='todolists',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='todolisttasks',
            old_name='to_do_list_id',
            new_name='to_do_list',
        ),
    ]