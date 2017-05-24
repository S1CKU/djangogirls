# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-08 09:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul', models.CharField(max_length=100)),
                ('data_wydania', models.DateField()),
                ('liczba_gwiazdek', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Muzyk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=50)),
                ('nazwisko', models.CharField(max_length=50)),
                ('pseudonim', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artysta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pierwsza.Muzyk'),
        ),
    ]
