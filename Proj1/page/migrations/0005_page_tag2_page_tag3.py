# Generated by Django 5.0.4 on 2024-05-04 14:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_page_tag1'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='tag2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tag2', to='page.pagetag'),
        ),
        migrations.AddField(
            model_name='page',
            name='tag3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tag3', to='page.pagetag'),
        ),
    ]
