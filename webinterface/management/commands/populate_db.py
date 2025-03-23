from django.core.management.base import BaseCommand
from faker import Faker
from webinterface.models import Sensor, SensorData, WifiConfig, Actor
import random

## @brief Populates the database with fake data.
class Command(BaseCommand):
    help = 'Populates the database with fake data'

    ## @brief Handles the command execution.
    #  @param args Command arguments.
    #  @param options Command options.
    def handle(self, *args, **options):
        fake = Faker()

        self.stdout.write(self.style.SUCCESS('Successfully started populating the database...'))

        # Delete existing data
        SensorData.objects.all().delete()
        Sensor.objects.all().delete()
        Actor.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted existing data'))

        # Create a WifiConfig object if one doesn't exist
        if not WifiConfig.objects.exists():
            wifi_config = WifiConfig(ssid=fake.word(), password=fake.password())
            wifi_config.save()
            self.stdout.write(self.style.SUCCESS('Successfully created WifiConfig object'))

        # Create some Sensor objects
        sensors = []
        for i in range(5):
            sensor = Sensor(sensor_type=fake.word(), sensor_name=fake.word())
            sensor.save()
            sensors.append(sensor)
            self.stdout.write(self.style.SUCCESS(f'Successfully created sensor: {sensor}'))

        # Create some SensorData objects
        for i in range(100):
            sensor = random.choice(sensors)
            value = {'temperature': fake.pyfloat(left_digits=2, right_digits=2, positive=True),
                     'humidity': fake.pyfloat(left_digits=2, right_digits=2, positive=True),
                     'soil_moisture': fake.pyfloat(left_digits=2, right_digits=2, positive=True)}
            thresholds = {key: fake.pyfloat(left_digits=2, right_digits=2, positive=True) for key in value}
            sensor_data = SensorData(sensor=sensor, value=value, thresholds=thresholds)
            sensor_data.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully created sensor data for sensor: {sensor}'))

        # Create some Actor objects
        for i in range(3):
            actor = Actor(actor_name=fake.word())
            actor.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully created actor: {actor}'))

        self.stdout.write(self.style.SUCCESS('Successfully populated the database!'))
