import adafruit_dht
import board
import time
import RPi.GPIO as GPIO

sensor = adafruit_dht.DHT11(board.D26)
GPIO.setmode(GPIO.BCM)
LED_PIN = 17
GPIO.setup(LED_PIN, GPIO.OUT)

try: 
    while True:
        temp_c = sensor.temperature
        humidity = sensor.humidity
        if humidity is not None and temp_c is not None:
            print(f'\nTemp in C: {temp_c}\nHumidity: {humidity}\n____________________')
            if temp_c > 23:
                GPIO.output(17, GPIO.HIGH)
                time.sleep(1)
                print("LED On")
            else: 
                print("LED Off")
        else:
            GPIO.output(17, GPIO.LOW)
            print("Sensor failure. Check wiring.")
        time.sleep(2)

except KeyboardInterrupt:
    print("Gracefully disconnecting.")
    GPIO.cleanup()

