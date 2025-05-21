import time

# Represents a relay actor
# This class simulates controlling a relay.
class Relay:
    def __init__(self, pin):
        """
        Initializes the Relay.
        Args:
            pin: The GPIO pin number to which the relay is connected.
        """
        self.pin = pin
        self.is_on = False  # Relay is initially off
        print(f"Relay on pin {self.pin} initialized. Current state: OFF")

    def turn_on(self):
        """
        Turns the relay ON.
        Returns:
            True if the operation was successful, False otherwise.
        """
        if not self.is_on:
            self.is_on = True
            # In a real scenario, this would involve setting the GPIO pin HIGH
            print(f"Relay on pin {self.pin} turned ON.")
            return True
        else:
            print(f"Relay on pin {self.pin} is already ON.")
            return False

    def turn_off(self):
        """
        Turns the relay OFF.
        Returns:
            True if the operation was successful, False otherwise.
        """
        if self.is_on:
            self.is_on = False
            # In a real scenario, this would involve setting the GPIO pin LOW
            print(f"Relay on pin {self.pin} turned OFF.")
            return True
        else:
            print(f"Relay on pin {self.pin} is already OFF.")
            return False

    def get_state(self):
        """
        Gets the current state of the relay.
        Returns:
            True if the relay is ON, False if it's OFF.
        """
        return self.is_on

if __name__ == '__main__':
    # Example usage:
    relay_pin = 17  # Assuming relay is connected to GPIO pin 17
    my_relay = Relay(pin=relay_pin)

    print(f"Initial relay state: {'ON' if my_relay.get_state() else 'OFF'}")

    my_relay.turn_on()
    time.sleep(1)  # Keep it on for 1 second

    my_relay.turn_on() # Try to turn on again
    time.sleep(1)

    my_relay.turn_off()
    time.sleep(1)

    my_relay.turn_off() # Try to turn off again

    print(f"Final relay state: {'ON' if my_relay.get_state() else 'OFF'}")
