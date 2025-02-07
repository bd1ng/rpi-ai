"""
AIPI 590
WEEK 1 LAB
___________________
BUTTON AUTOMATION

- Clone this code to your Raspberry Pi
- Fill in your code
- Push back to Edstem with Git

"""

import RPi.GPIO as GPIO
import time

# GPIO setup
GPIO.setmode(GPIO.BCM)

"""
PIN CONFIGURATION:
Add your button's GPIO pin below
"""

BUTTON_PIN = 21
LED_PIN = 20

#Setup the button as an input using a pull up resistor
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)

"""
CUSTOM FUNCTION
# ADD YOUR CODE TO THE DESIGNATED AREA BELOW
# DO NOT ALTER THE SURROUNDING CODE
"""

def button_callback(channel):
    print("Button Pressed!")
    ## START CUSTOM CODE
    if GPIO.output(LED_PIN, GPIO.HIGH):
        print("LED ON")
        time.sleep(1)
        GPIO.output(LED_PIN, GPIO.LOW)
        print("LED OFF")
        time.sleep(1)
    ## END CUSTOM CODE

# Add event detection
GPIO.add_event_detect(BUTTON_PIN, GPIO.RISING, callback=button_callback, bouncetime=200)

try:
    print("Press the button to trigger an action.")
    while True:
        time.sleep(0.1)  # Keep the script running
except KeyboardInterrupt:
    GPIO.cleanup()