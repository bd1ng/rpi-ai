"""
AIPI 590
WEEK 2 - LAB 2
___________________
BUTTON DEBOUNCING

- Clone this code to your Raspberry Pi
- Fill in the required functions
- Run your code
- If it passes, push back to Edstem with Git

"""

import RPi.GPIO as GPIO
import time

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)

# Counter for button presses
callback_counter = 0

"""
PIN CONFIGURATION:
Add your button's GPIO pin below
"""
button_pin = 21

"""
S0LUTION FUNCTION
# ADD YOUR SOLUTION TO THE DESIGNATED AREA
# DO NOT ALTER THE SURROUNDING CODE
"""

def configure_button():
    """
    Configure the GPIO pin for button input with a 
    pull-up or pull-down resistor depending on your setup.

    """
    ### BEGIN SOLUTION ###

    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    ### END SOLUTION ###

"""
S0LUTION FUNCTION
# ADD YOUR SOLUTION TO THE DESIGNATED AREA
# DO NOT ALTER THE SURROUNDING CODE
"""

def configure_debouncing():
    """
    Configure event detection on the button pin with debouncing.
    - Use GPIO.FALLING if you're using a pull-up resistor
    - Use GPIO.RISING if you're using a pull-down resistor
    - The "button_callback" callback function has been created for you to use.
    - Start with a 200ms bounce time.

    """
    ### BEGIN SOLUTION ###
    
    GPIO.add_event_detect(button_pin, GPIO.RISING, callback=button_callback, bouncetime=200)

    ### END SOLUTION ###

"""
TEST FUNCTION:
DO NOT REMOVE OR EDIT
AND CODE BELOW THIS line
___________________
"""

def button_callback(channel):
    global callback_counter
    callback_counter += 1
    print("Button Pressed!")

try:
    # Configure button and debouncing
    configure_button()  # TODO: Call the function to configure the button
    configure_debouncing()  # TODO: Call the function to configure debouncing
    print("\nPress the button 4 times in the next\n10 seconds. Then wait to see if you pass.\n-----------------------")
    time.sleep(10)  # Allow time for the user to press the button

    # Validate the number of button presses
    assert callback_counter == 4, f"Expected 4 presses, but got {callback_counter}."
    print("Button debouncing test passed!")
except KeyboardInterrupt:
    print("Exiting program.")
finally:
    GPIO.cleanup()


