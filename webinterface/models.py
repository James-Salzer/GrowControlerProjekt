from django.db import models
from django.conf import settings

## @brief Model for storing sensor data.
class SensorData(models.Model):
    ## @brief The sensor to which this data belongs.
    sensor = models.ForeignKey(
        'Sensor',
        on_delete=models.CASCADE,
        related_name='sensor_data',
        default=1  # Set a default value
    )
    ## @brief The timestamp when the sensor data was recorded.
    timestamp = models.DateTimeField(auto_now_add=True)
    ## @brief The sensor value as a JSON object.
    value = models.JSONField()
    ## @brief The threshold values as a JSON object.
    thresholds = models.JSONField(default=dict)

    ## @brief Returns a string representation of the sensor data.
    def __str__(self):
        return f"Sensor Data - {self.timestamp}"

    class Meta:
        get_latest_by = 'timestamp'

## @brief Model for storing WiFi configuration.
class WifiConfig(models.Model):
    ## @brief The SSID of the WiFi network.
    ssid = models.CharField(max_length=255)
    ## @brief The password of the WiFi network.
    password = models.CharField(max_length=255)

    ## @brief Returns a string representation of the WiFi configuration.
    def __str__(self):
        return f"Wifi Config - {self.ssid}"

## @brief Model for storing sensor information.
class Sensor(models.Model):
    ## @brief The name/type of the sensor (e.g., temp/humidity, soilmoisture-sensor).
    sensor_type = models.CharField(max_length=255)
    ## @brief The specific name of the sensor (e.g., DHT11, DHT22, BH1750).
    sensor_name = models.CharField(max_length=255)
    ## @brief The date and time of the sensor's first installation.
    installation_date = models.DateTimeField(auto_now_add=True)

    ## @brief Returns a string representation of the sensor.
    def __str__(self):
        return f"Sensor: {self.sensor_type} ({self.sensor_name})"

## @brief Model for storing actor information.
class Actor(models.Model):
    ## @brief The name of the actor (e.g., water pump, light, ventilator).
    actor_name = models.CharField(max_length=255)
    ## @brief The date and time of the actor's first installation.
    installation_date = models.DateTimeField(auto_now_add=True)
    ## @brief The current on/off state of the actor.
    is_on = models.BooleanField(default=False)
    ## @brief The date and time when the actor's state was last changed.
    last_changed = models.DateTimeField(auto_now=True)

    ## @brief Returns a string representation of the actor.
    def __str__(self):
        return f"Actor: {self.actor_name}"
