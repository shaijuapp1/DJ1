# Generated by Django 5.0.4 on 2024-05-04 09:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebDocTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='WebDoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('url', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('det1', models.TextField()),
                ('d2t2', models.TextField()),
                ('tag1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='todo.webdoctag')),
            ],
        ),
    ]
