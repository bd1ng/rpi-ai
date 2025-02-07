# import packages

import RPi.GPIO as GPIO
import time
from lcd_i2c import LCD_I2C
import smbus

# set-up GPIO
GPIO.setmode(GPIO.BCM)

# I2C setup
I2C_BUS = 1  # Use I2C bus 1
DEVICE_ADDRESS = 0x4b  # Default I2C address for ADS7830
bus = smbus.SMBus(I2C_BUS)

# read adc
def read_adc():    
    channel = 0
    if channel < 0 or channel > 7:
        raise ValueError("Channel must be between 0 and 7")
    control_byte = 0x84 | (channel << 4) 
    bus.write_byte(DEVICE_ADDRESS, control_byte)
    data = bus.read_byte(DEVICE_ADDRESS)
    return data

# pwm set-up
led_pin = 13
def configure_pwm():
    global pwm
    GPIO.setup(led_pin, GPIO.OUT)
    pwm = GPIO.PWM(led_pin, 100)
    pwm.start(0)

def change_brightness(duty_cycle):
    if 0 <= duty_cycle <= 100:
        pwm.ChangeDutyCycle(duty_cycle)
    else: print("No no, duty cycle must be between 0 and 100!")

# config lcd
def configure_i2c_lcd():
    global lcd
    lcd = LCD_I2C(0x27, 16, 2)
    lcd.backlight.on()

def write_to_lcd():
    lcd.cursor.setPos(0,0)
    lcd.write_text('Brightness:')
    lcd.cursor.setPos(1,0)
    lcd.write_text(f"{duty_cycle:.2f}")

# def clean-up
def cleanup():
    lcd.backlight.off()
    lcd.clear()
    GPIO.cleanup()  


# def brightness

try:
    configure_i2c_lcd() 
    configure_pwm()

    while True:
        adc_value = read_adc()
        duty_cycle = (adc_value / 255) * 100  # Convert to 0-100 range
        change_brightness(duty_cycle)
        write_to_lcd()
        time.sleep(0.5)  # Add a short delay to avoid overwhelming the LCD

except KeyboardInterrupt:
    print("Interrupted by user. Exiting...")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    cleanup()
    bus.close()


