"""
AIPI 590
WEEK 2 - LAB 5
___________________
ANALOG TO DIGITAL CONVERSION (ADC)

- Clone this code to your Raspberry Pi
- Fill in the required functions
- Run your code
- If it passes, push back to Edstem with Git
"""

import smbus

# I2C configuration
I2C_BUS = 1  # Use I2C bus 1

"""
DEVICE CONFIGURATION:
Add the devices address
You can find it through i2cdetect -y 1
Remember that the value should be HEX ex. 0x00
"""
DEVICE_ADDRESS = 0x4b

# Create SMBus instance
bus = smbus.SMBus(I2C_BUS)

"""
SOLUTION FUNCTION:
# ADD YOUR SOLUTION TO THE DESIGNATED AREA
# DO NOT ALTER THE SURROUNDING CODE
"""

def read_adc():
    """
    Reads the analog value from the specified channel (0-7).
    
    Create a variable called 'channel'
     - Set it to your input channel.
     - It should be an int between 0 and 7
     - On the ADC, it will be labeld A0-A7

    Create a control_byte variable that contains the values
    to send a single-ended operation control byte

    Use 'bus.write_byte(DEVICE_ADDRESS, control_byte)' to send
    the control byte to the ADC.

    Create a variable called 'data' that is equal to
    'bus.read_byte(DEVICE_ADDRESS) so that you can capture the data.

    Return 'data'
    """
    ### BEGIN SOLUTION ###
    
    channel = 0

    if channel < 0 or channel > 7:
        raise ValueError("Channel must be between 0 and 7")

    control_byte = 0x84 | (channel << 4) 
    bus.write_byte(DEVICE_ADDRESS, control_byte)
    data = bus.read_byte(DEVICE_ADDRESS)
    return data

    ### END SOLUTION ###

"""
TEST FUNCTION:
DO NOT REMOVE OR EDIT
AND CODE BELOW THIS LINE
___________________
"""

def test_adc():
    """
    Tests the ADC read function by checking if values are in the expected range.
    """
    print(f"Testing ADC...")
    try:
        value = read_adc()
        assert 0 <= value <= 255, f"Value {value} out of expected range (0-255)."
        print(f"ADC Test Passed! Value read: {value}")
    except Exception as e:
        print(f"Test Failed: {e}")

try:
    # Run the ADC test
    test_adc()
except KeyboardInterrupt:
    print("Exiting program.")
finally:
    bus.close()

