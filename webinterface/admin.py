from django.contrib import admin
from .models import SensorData, WifiConfig, Sensor, Actor

## @brief Registers the SensorData model in the admin interface.
admin.site.register(SensorData)
## @brief Registers the WifiConfig model in the admin interface.
admin.site.register(WifiConfig)
admin.site.register(Sensor)
admin.site.register(Actor)
