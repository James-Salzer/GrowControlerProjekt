from django.contrib import admin
from .models import SensorData, WifiConfig

## @brief Registers the SensorData model in the admin interface.
admin.site.register(SensorData)
## @brief Registers the WifiConfig model in the admin interface.
admin.site.register(WifiConfig)
