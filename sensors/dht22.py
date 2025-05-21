import random

# Represents the DHT22 sensor
# This class simulates reading temperature and humidity data from a DHT22 sensor.
class DHT22:
    def __init__(self, pin):
        """
        Initializes the DHT22 sensor.
        Args:
            pin: The GPIO pin number to which the sensor is connected.
        """
        self.pin = pin

    def read(self):
        """
        Reads temperature and humidity data from the sensor.
        Returns:
            A tuple containing temperature (Celsius) and humidity (%).
            Returns (None, None) if reading fails.
        """
        # Simulate reading data from the sensor
        # In a real scenario, this would involve interacting with the hardware.
        temperature = random.uniform(20, 30)  # Simulate temperature between 20-30°C
        humidity = random.uniform(40, 60)   # Simulate humidity between 40-60%

        # Simulate potential sensor error
        if random.random() < 0.1:  # 10% chance of error
            return (None, None)

        return (temperature, humidity)

if __name__ == '__main__':
    # Example usage:
    sensor = DHT22(pin=4)  # Assuming sensor is connected to GPIO pin 4
    temperature, humidity = sensor.read()

    if temperature is not None and humidity is not None:
        print(f"Temperature: {temperature:.2f}°C")
        print(f"Humidity: {humidity:.2f}%")
    else:
        print("Failed to read data from sensor.")
