# Generated by Django 5.1.7 on 2025-03-23 10:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webinterface", "0005_sensordata_sensor"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="sensordata",
            name="humidity",
        ),
        migrations.RemoveField(
            model_name="sensordata",
            name="soil_moisture",
        ),
        migrations.RemoveField(
            model_name="sensordata",
            name="temperature",
        ),
        migrations.AddField(
            model_name="sensordata",
            name="value",
            field=models.JSONField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="sensordata",
            name="sensor",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sensor_data",
                to="webinterface.sensor",
            ),
        ),
    ]
