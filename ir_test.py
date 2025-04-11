# Required modules are imported
from gpiozero import LED
import time

# Initialize the LED on pin 15
led = LED(15)

print("LED test [press CTRL+C to end the test]")

# Main program loop
try:
    while True:
        print("LED on for 4 seconds")
        led.on()  # LED is switched on
        time.sleep(4)  # Wait mode for 4 seconds
        print("LED 2 Sekunden aus")
        led.off()  # LED is switched off
        time.sleep(2)  # Waiting mode for a further two seconds, during which the LED is then switched off

# Clean up after the program has been completed
except KeyboardInterrupt:
    led.close()  # Release of resources
