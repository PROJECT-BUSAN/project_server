# Generated by Django 3.2.7 on 2021-09-20 09:35

import activity.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_auto_20210910_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitydetail',
            name='activity_file',
            field=models.FileField(blank=True, null=True, upload_to=activity.models.get_file_path, verbose_name='활동파일'),
        ),
    ]