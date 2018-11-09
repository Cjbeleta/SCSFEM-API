# Generated by Django 2.1.2 on 2018-11-08 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_equipmentreservation_facilityreservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=150)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('usertype', models.IntegerField(default=2)),
                ('token_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Token')),
            ],
        ),
    ]