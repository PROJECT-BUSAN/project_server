# Generated by Django 3.2.7 on 2021-09-14 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
