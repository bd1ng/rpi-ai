"""
AIPI 590
WEEK 2 - LAB 4
___________________
PIN PROTOCOLS: CONNECTING A 16x2 I2C LCD SCREEN

- Clone this code to your Raspberry Pi
- Fill in the required functions
- Run your code
"""

# Import necessary libraries
from lcd_i2c import LCD_I2C

# Global LCD object
lcd = None

"""
SOLUTION FUNCTION:
# ADD YOUR SOLUTION TO THE DESIGNATED AREA
# DO NOT ALTER THE SURROUNDING CODE
"""

def configure_i2c_lcd():
    """
    Configures the 16x2 I2C LCD screen.

    Set the global 'lcd' variable equal to LCD_I2C(address, columns, rows)
    Where:
    - address (int): The I2C address of the LCD through i2cdetect (e.g., 0x27 or 0x39).
    - columns (int): The number of columns on the LCD (typically 16).
    - rows (int): The number of rows on the LCD (typically 2).

    You can also try turning the backlight on and the cursor on.
    - lcd.backlight.on()
    - lcd.blink.on()
    """
    global lcd
    ### BEGIN SOLUTION ###
    lcd = LCD_I2C(0x27, 16, 2)
    lcd.backlight.on()
    lcd.blink.on()
    ### END SOLUTION ###

"""
SOLUTION FUNCTION:
# ADD YOUR SOLUTION TO THE DESIGNATED AREA
# DO NOT ALTER THE SURROUNDING CODE
"""

def write_to_lcd():
    """
    Writes text to the LCD screen.

    Use lcd.cursor.setPos(row, col) to set the positon of
    where to write the text.
    
    Use lcd.write_text('string') to write text starting at
    the cursor location.
    """
    ### BEGIN SOLUTION ###
    lcd.cursor.setPos(0,0)
    lcd.write_text('Gaining')
    lcd.cursor.setPos(1,0)
    lcd.write_text('Sentience...')
    ### END SOLUTION ###

"""
TEST FUNCTION:
DO NOT REMOVE OR EDIT
AND CODE BELOW THIS LINE
___________________
"""

def cleanup():
    """
    Cleans up the LCD and GPIO resources.
    """
    lcd.backlight.off()
    lcd.clear()


try:
    # Configure the LCD with the appropriate I2C address
    configure_i2c_lcd() 
    # Write messages to the LCD
    write_to_lcd()
    
    # Wait and show the message for 10 seconds
    input("Press Enter to exit after observing the display...")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if lcd:
        lcd.backlight.off()
        lcd.clear()

