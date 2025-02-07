import RPi.GPIO as GPIO
import time

# Setup GPIO
GPIO.setmode(GPIO.BCM)
button_pin = 18
led_pin = 21

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led_pin, GPIO.OUT)

# Main loop
try:
    while True:
        if GPIO.input(button_pin):
            GPIO.output(led_pin, True)  # LED ON
            print("button pushed")
        else:
            GPIO.output(led_pin, False) # LED OFF
            print('button released')
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Gracefully disconnecting.")

finally:
    GPIO.cleanup()  # This ensures cleanup always runs
    print("GPIO cleanup done!")