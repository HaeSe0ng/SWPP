# Generated by Django 2.2.5 on 2019-11-02 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='firstName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='emailPublic',
            new_name='is_email_public',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='interestPublic',
            new_name='is_interest_public',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='schedulePublic',
            new_name='is_schedule_public',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='lastName',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='phoneNumber',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='profilePicture',
            new_name='profile_picture',
        ),
    ]
