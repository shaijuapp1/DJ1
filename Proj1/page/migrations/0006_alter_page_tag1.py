# Generated by Django 5.0.4 on 2024-05-04 14:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_page_tag2_page_tag3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='tag1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tag1', to='page.pagetag'),
        ),
    ]
