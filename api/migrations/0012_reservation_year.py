# Generated by Django 2.1.2 on 2018-12-02 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20181202_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='year',
            field=models.IntegerField(default=2018),
        ),
    ]
