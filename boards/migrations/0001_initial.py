# Generated by Django 3.2.7 on 2021-10-09 11:57

import boards.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, null=True, unique=True)),
                ('is_anonymous', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('top_fixed', models.BooleanField(default=False)),
                ('only_superuser', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '게시판 종류',
                'verbose_name_plural': '게시판 종류 모음',
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': '댓글',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, null=True)),
                ('content', models.TextField(default='')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='post_thumbnail/')),
                ('hits', models.PositiveIntegerField(default=0)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('top_fixed', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '게시글',
                'verbose_name_plural': '게시글 모음',
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='PostFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_files', models.FileField(blank=True, null=True, upload_to=boards.models.get_file_path, verbose_name='파일')),
                ('filename', models.CharField(max_length=64, null=True, verbose_name='첨부파일명')),
            ],
            options={
                'verbose_name': '첨부파일',
                'verbose_name_plural': '첨부파일 모음',
                'ordering': ['-post__created_date'],
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='reply', to='boards.comment')),
            ],
            options={
                'verbose_name_plural': '대댓글',
            },
        ),
    ]
