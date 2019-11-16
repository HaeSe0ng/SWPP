# Generated by Django 2.2.5 on 2019-11-16 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matchmaker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='additional_info',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='match',
            name='location_latitude',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='match',
            name='location_longitude',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='match',
            name='location_text',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='match',
            name='match_thumbnail',
            field=models.ImageField(blank=True, default='thumbnail/default-user.png', null=True, upload_to='thumbnail/'),
        ),
    ]
