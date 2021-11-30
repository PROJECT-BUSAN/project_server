# Generated by Django 3.2.7 on 2021-11-26 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20211127_0409'),
    ]

    operations = [
        migrations.AddField(
            model_name='applier',
            name='is_favor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='applier',
            name='is_picked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='applier',
            name='apply_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]