# Generated by Django 5.0.4 on 2024-05-04 11:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_webdoctag_webdoc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webdoc',
            name='tag1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='todo.webdoctag'),
        ),
    ]