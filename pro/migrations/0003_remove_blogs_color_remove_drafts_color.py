# Generated by Django 4.2.14 on 2024-08-04 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro', '0002_blogs_drafts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='color',
        ),
        migrations.RemoveField(
            model_name='drafts',
            name='color',
        ),
    ]