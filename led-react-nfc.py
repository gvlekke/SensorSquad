import board
import neopixel
import time
import busio
from adafruit_pn532.i2c import PN532_I2C

LED_PIN = board.D18 # GPIO 18
LED_COUNT = 30

strip = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=0.1, auto_write=False)

strip.fill((50, 0, 0))  # Set all LEDs to Red
strip.show()


# Initialize I2C connection
i2c = busio.I2C(board.SCL, board.SDA)
pn532 = PN532_I2C(i2c, debug=False)

# Get firmware version from PN532
ic, ver, rev, support = pn532.firmware_version
print(f"Found PN532 with firmware version: {ver}.{rev}")

# Configure PN532 to communicate with tags
pn532.SAM_configuration()

print("Waiting for an NFC card...")

while True:
    uid = pn532.read_passive_target(timeout=0.5)
    if uid is not None:
        hex = uid.hex()
        # Wipe LED strip with Green
        for i in range(LED_COUNT):
            strip[i] = (int(hex[:2], 16), int(hex[2:4], 16), int(hex[4:6], 16))
            strip.show()
            time.sleep(0.05)

        print(f"Found NFC card with UID: {uid.hex()}")

        time.sleep(1)
        for i in range(LED_COUNT):
            strip[i] = (0,0,0)
            strip.show()
            time.sleep(0.01)
