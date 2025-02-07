"""
AIPI 590
WEEK 2 LAB - MODULE 2
___________________
PULL UP & PULL DOWN RESISTORS

- Clone this code to your Raspberry Pi
- Fill in the required functions
- Run your code
- If it passes, push back to Edstem with Git

"""

import RPi.GPIO as GPIO
import time

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)



button_pin = 18

"""
S0LUTION FUNCTION:
# ADD YOUR SOLUTION TO THE DESIGNATED AREA
# DO NOT ALTER THE SURROUNDING CODE
"""

def configure_pull_up():
    """
    Configure the GPIO pin for button input with a pull-up resistor.
    
    """
    ### BEGIN SOLUTION ###
    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    return
    ### END SOLUTION ###

"""
S0LUTION FUNCTION:
# ADD YOUR SOLUTION TO THE DESIGNATED AREA
# DO NOT ALTER THE SURROUNDING CODE
"""

def configure_pull_down():
    """
    Configure the GPIO pin for button input with a pull-down resistor.

    """
    ### BEGIN SOLUTION ###
    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    return
    ### END SOLUTION ###

"""
TEST FUNCTION:
DO NOT REMOVE OR EDIT
AND CODE BELOW THIS LINE
___________________
"""

def test_button_press(expected_state):
    button_state = GPIO.input(button_pin)
    assert button_state == expected_state, f"Expected {expected_state}, but got {button_state}"

try:
    # Allow user to choose configuration
    choice = input("Choose configuration to test (1: Pull-Up, 2: Pull-Down): ").strip()

    if choice == '1':
        print("Here 1")
        print("Configuring pull-up resistor...")
        configure_pull_up()
        print("Here 2")
        input("Press the button (expected: LOW). Press Enter when ready...")
        test_button_press(GPIO.LOW)
        print("Here 3")
    elif choice == '2':
        print("Configuring pull-down resistor...")
        configure_pull_down()
        input("Press the button (expected: HIGH). Press Enter when ready...")
        test_button_press(GPIO.HIGH)
    else:
        print("Invalid choice. Please restart the program and choose 1 or 2.")

    print("All tests passed!")
except AssertionError as e:
    print(f"Test failed: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    GPIO.cleanup()

