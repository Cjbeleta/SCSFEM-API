# Generated by Django 2.1.2 on 2018-12-02 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20181202_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventname', models.TextField(default=' ')),
                ('quantity', models.IntegerField(default=0)),
                ('date_application', models.DateField(auto_now_add=True)),
                ('year', models.IntegerField(default=2018)),
                ('month', models.IntegerField(default=0)),
                ('start_day', models.IntegerField(default=0)),
                ('end_day', models.IntegerField(default=0)),
                ('start_time', models.IntegerField(default=0)),
                ('end_time', models.IntegerField(default=0)),
                ('status', models.IntegerField(default=0)),
                ('borrower_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Borrower')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Facility')),
            ],
        ),
        migrations.RemoveField(
            model_name='equipmentreservation',
            name='borrower_id',
        ),
        migrations.RemoveField(
            model_name='equipmentreservation',
            name='item_id',
        ),
        migrations.RemoveField(
            model_name='facilityreservation',
            name='borrower_id',
        ),
        migrations.RemoveField(
            model_name='facilityreservation',
            name='item_id',
        ),
        migrations.DeleteModel(
            name='EquipmentReservation',
        ),
        migrations.DeleteModel(
            name='FacilityReservation',
        ),
    ]
