# Generated by Django 5.1.7 on 2025-03-23 10:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webinterface", "0004_actor_sensor"),
    ]

    operations = [
        migrations.AddField(
            model_name="sensordata",
            name="sensor",
            field=models.ForeignKey(
                default=2,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sensor_data",
                to="webinterface.sensor",
            ),
            preserve_default=False,
        ),
    ]
