# Generated by Django 5.0.4 on 2024-05-04 13:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='tag1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tag1', to='page.pagetag'),
        ),
        migrations.AlterField(
            model_name='page',
            name='tag2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tag2', to='page.pagetag'),
        ),
        migrations.AlterField(
            model_name='page',
            name='tag3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tag3', to='page.pagetag'),
        ),
    ]