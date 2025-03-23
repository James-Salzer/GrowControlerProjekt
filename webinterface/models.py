from django.db import models
from django.conf import settings

## @brief Model for storing sensor data.
class SensorData(models.Model):
    ## @brief The timestamp when the sensor data was recorded.
    timestamp = models.DateTimeField(auto_now_add=True)
    ## @brief The temperature reading.
    temperature = models.FloatField()
    ## @brief The humidity reading.
    humidity = models.FloatField()
    ## @brief The soil moisture reading.
    soil_moisture = models.FloatField()

    ## @brief Returns a string representation of the sensor data.
    def __str__(self):
        return f"Sensor Data - {self.timestamp}"

## @brief Model for storing WiFi configuration.
class WifiConfig(models.Model):
    ## @brief The SSID of the WiFi network.
    ssid = models.CharField(max_length=255)
    ## @brief The password of the WiFi network.
    password = models.CharField(max_length=255)

    ## @brief Returns a string representation of the WiFi configuration.
    def __str__(self):
        return f"Wifi Config - {self.ssid}"
