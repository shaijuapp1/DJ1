# Generated by Django 5.0.4 on 2024-05-04 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_alter_page_tag1_alter_page_tag2_alter_page_tag3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='tag1',
        ),
        migrations.RemoveField(
            model_name='page',
            name='tag2',
        ),
        migrations.RemoveField(
            model_name='page',
            name='tag3',
        ),
        migrations.AlterField(
            model_name='page',
            name='d2t2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='det1',
            field=models.TextField(blank=True, null=True),
        ),
    ]
