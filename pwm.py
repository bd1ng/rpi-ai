"""
AIPI 590
WEEK 2 - LAB 3
___________________
PULSE WIDTH MODULATION (PWM)

- Clone this code to your Raspberry Pi
- Fill in the required functions
- Run your code
- If it passes, push back to Edstem with Git
"""

import RPi.GPIO as GPIO
import time

# GPIO setup
GPIO.setmode(GPIO.BCM)

"""
PIN CONFIGURATION:
Add your LED's GPIO pin below
*PWM GPIO pins are 12,13,18 and 19
"""
led_pin = 13

# Global PWM object
pwm = None

"""
SOLUTION FUNCTION:
# ADD YOUR SOLUTION TO THE DESIGNATED AREA
# DO NOT ALTER THE SURROUNDING CODE
"""

def configure_pwm():
    """
    - Sets up the LED GPIO pin
    - Configures the GPIO pin for PWM output.
    - Start the PWM 0% duty cycle
    """
    global pwm
    ### BEGIN SOLUTION ###

    GPIO.setup(led_pin, GPIO.OUT)
    pwm = GPIO.PWM(led_pin, 100)
    pwm.start(0)

    ### END SOLUTION ###

"""
SOLUTION FUNCTION:
# ADD YOUR SOLUTION TO THE DESIGNATED AREA
# DO NOT ALTER THE SURROUNDING CODE
"""

def change_brightness(duty_cycle):
    """
    Args: duty_cycle (int)

    - Use pwm's "ChangeDutyCyle" class to
      changes the brightness of the LED.
    - Could also include an 'if' statement that
      ensures the duty cycle is between 0-100
        
    """
    ### BEGIN SOLUTION ###
 
    if 0 <= duty_cycle <= 100:
        pwm.ChangeDutyCycle(duty_cycle)
    else: print("No no, duty cycle must be between 0 and 100!")

    ### END SOLUTION ###

"""
TEST FUNCTION:
DO NOT REMOVE OR EDIT
AND CODE BELOW THIS LINE
___________________
"""

def test_pwm():
    """
    Tests the PWM configuration and brightness adjustment.
    """
    print("Testing PWM configuration and brightness control...")
    try:
        # Test PWM setup
        configure_pwm()
        print("PWM configured successfully.")

        # Test brightness adjustment
        change_brightness(50)
        time.sleep(2)  # Hold brightness for 2 seconds
        change_brightness(10)
        time.sleep(2)
        change_brightness(100)
        time.sleep(2)

        print("PWM test passed!")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        if pwm:
            pwm.stop()
        GPIO.cleanup()

try:
    # Run the PWM test
    test_pwm()
except KeyboardInterrupt:
    print("Exiting program.")
finally:
    GPIO.cleanup()

