# Generated by Django 3.2.7 on 2021-11-26 22:53

from django.db import migrations, models
import django.db.models.deletion
import survey.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_auto_20211127_0725'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apply_file', models.FileField(blank=True, null=True, upload_to=survey.models.get_file_path, verbose_name='파일')),
                ('filename', models.CharField(max_length=128, null=True, verbose_name='첨부파일명')),
                ('applier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applyfile', to='survey.applier')),
            ],
            options={
                'verbose_name': '지원서 첨부파일',
                'verbose_name_plural': '지원서 첨부파일',
            },
        ),
        migrations.DeleteModel(
            name='SurveyFile',
        ),
    ]