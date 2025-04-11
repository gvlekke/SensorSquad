import RPi.GPIO as GPIO
import time

# Set up GPIO pin numbers
IR_TRANSMITTER_PIN = 14  # GPIO pin for KY005 transmitter
IR_RECEIVER_PIN = 15     # GPIO pin for KY022 receiver

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set up GPIO pins
GPIO.setup(IR_TRANSMITTER_PIN, GPIO.OUT)
GPIO.setup(IR_RECEIVER_PIN, GPIO.IN)

try:
    print("IR monitoring started. Press CTRL+C to exit.")
    last_state = None
    
    # Continuously transmit IR signal
    GPIO.output(IR_TRANSMITTER_PIN, GPIO.HIGH)
    
    # Monitor the receiver
    while True:
        # Read the state of the IR receiver
        # When signal is received, the pin will be LOW (0)
        # When signal is blocked, the pin will be HIGH (1)
        current_state = GPIO.input(IR_RECEIVER_PIN)
        
        # Update output only when state changes to avoid flooding the console
        if current_state != last_state:
            if current_state == 0:  # Signal received
                print("received")
            else:  # Signal blocked
                print("blocked")
            
            last_state = current_state
        
        time.sleep(0.1)  # Small delay to prevent CPU overuse

except KeyboardInterrupt:
    print("\nProgram stopped by user")
finally:
    # Clean up GPIO settings
    GPIO.output(IR_TRANSMITTER_PIN, GPIO.LOW)
    GPIO.cleanup()