# Generated by Django 3.2.7 on 2021-10-09 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='기관명', max_length=30)),
                ('urlname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField(help_text='온도')),
                ('day', models.DateField(help_text='날짜')),
                ('time', models.TimeField(help_text='시간')),
                ('organ', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organ', to='sotongapp.organ')),
            ],
        ),
    ]
