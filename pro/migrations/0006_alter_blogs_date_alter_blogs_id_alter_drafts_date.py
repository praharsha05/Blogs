# Generated by Django 4.2.14 on 2024-08-26 17:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro', '0005_blogs_date_drafts_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 26, 17, 22, 26, 584305, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='drafts',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 26, 17, 22, 26, 584702, tzinfo=datetime.timezone.utc)),
        ),
    ]