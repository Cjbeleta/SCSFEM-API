# Generated by Django 2.1.2 on 2018-11-16 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20181116_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='description',
            field=models.TextField(default='None'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='image',
            field=models.TextField(default='https://images.unsplash.com/photo-1531988042231-d39a9cc12a9a?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=a562d48d64fd49e7cd0419f70806d696&auto=format&fit=crop&w=750&q=80'),
        ),
    ]
