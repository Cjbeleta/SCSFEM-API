# Generated by Django 2.1.2 on 2018-12-08 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='item_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='schedule',
            name='item_type',
            field=models.IntegerField(default=0),
        ),
    ]
