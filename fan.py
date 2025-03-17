import RPi.GPIO as GPIO
import time
from lcd_i2c import LCD_I2C
import smbus
import threading

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
# adc value will be between 0-255

# stepper set-up
IN1 = 17
IN2 = 27
IN3 = 22
IN4 = 23

step_sequence = [
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 1]
]

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Helper function to set motor step
def set_step(step):
    GPIO.output(IN1, step[0])
    GPIO.output(IN2, step[1])
    GPIO.output(IN3, step[2])
    GPIO.output(IN4, step[3])

# Rotate motor
def rotate_motor(steps, delay=0.01):
    for _ in range(int(steps)):
        for step in step_sequence:
            set_step(step)
            time.sleep(delay)

# LCD
def configure_i2c_lcd():
    global lcd
    lcd = LCD_I2C(0x27, 16, 2)
    lcd.backlight.on()

def update_display():
    """ Continuously updates the LCD display independently """
    while True:
        adc_value = read_adc()
        display = adc_value  # Adjust scaling if needed
        lcd.cursor.setPos(1, 0)
        lcd.write_text(f"{display:.2f}°")
        time.sleep(0.1)  # Update the display every 100ms


configure_i2c_lcd() 
lcd.cursor.setPos(0,0)
lcd.write_text('Rotation:')

current_position = 0
last_display_update = 0
last_motor_update = 0

try:
    current_position = 0
    
    while True:
        adc_value = read_adc()
        current_time = time.time()

        if current_time - last_display_update >= 0.1:
            display = adc_value/255*360
            lcd.cursor.setPos(1, 0)
            lcd.write_text(f"{display:.2f}°")
            last_display_update = current_time
        
        if current_time - last_motor_update >= 0.1:
            steps = (current_position - adc_value) / 255 * 512
            if abs(steps) > 1:
                rotate_motor(int(steps))
                current_position = adc_value
            else:
                print("No significant change, stopping motor.")
            last_motor_update = current_time 

        time.sleep(0.01) 

except KeyboardInterrupt:
    print("Exiting...")
    bus.close()
    GPIO.cleanup()