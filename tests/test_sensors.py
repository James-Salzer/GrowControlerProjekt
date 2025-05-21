import unittest
from unittest.mock import patch
import sys
import os

# Adjust the path to include the parent directory (project root)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sensors.dht22 import DHT22

class TestDHT22Sensor(unittest.TestCase):

    def test_sensor_initialization(self):
        """Test that the DHT22 sensor initializes correctly."""
        sensor = DHT22(pin=4)
        self.assertEqual(sensor.pin, 4, "Sensor pin should be initialized.")
        print("TestSensorInitialization: PASSED")

    @patch('sensors.dht22.random.uniform')
    @patch('sensors.dht22.random.random')
    def test_successful_read(self, mock_random_error_check, mock_uniform_reading):
        """Test a successful read of temperature and humidity."""
        # Configure mocks
        # No error occurs (random.random() returns value >= 0.1)
        mock_random_error_check.return_value = 0.5
        # Simulate temperature and humidity readings
        mock_uniform_reading.side_effect = [25.5, 55.5] # temp, hum

        sensor = DHT22(pin=4)
        temperature, humidity = sensor.read()

        self.assertIsNotNone(temperature, "Temperature should not be None on successful read.")
        self.assertIsNotNone(humidity, "Humidity should not be None on successful read.")
        self.assertEqual(temperature, 25.5, "Temperature reading is incorrect.")
        self.assertEqual(humidity, 55.5, "Humidity reading is incorrect.")
        
        mock_uniform_reading.assert_any_call(20, 30) # Check if temperature range is correct
        mock_uniform_reading.assert_any_call(40, 60) # Check if humidity range is correct
        print("TestSuccessfulRead: PASSED")

    @patch('sensors.dht22.random.random')
    def test_sensor_read_failure(self, mock_random_error_check):
        """Test a sensor read failure scenario."""
        # Configure mock for error occurrence (random.random() returns value < 0.1)
        mock_random_error_check.return_value = 0.05 # Simulate an error

        sensor = DHT22(pin=4)
        temperature, humidity = sensor.read()

        self.assertIsNone(temperature, "Temperature should be None when sensor read fails.")
        self.assertIsNone(humidity, "Humidity should be None when sensor read fails.")
        print("TestSensorReadFailure: PASSED")

if __name__ == '__main__':
    unittest.main()
