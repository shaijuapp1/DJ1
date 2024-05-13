# Generated by Django 5.0.4 on 2024-05-04 14:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_remove_page_tag1_remove_page_tag2_remove_page_tag3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='tag1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tag1', to='page.pagetag'),
        ),
    ]