# Generated by Django 3.2.7 on 2021-09-08 11:44

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=froala_editor.fields.FroalaField(blank=True, null=True),
        ),
    ]