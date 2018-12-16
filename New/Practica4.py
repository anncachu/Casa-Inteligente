import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
#print ("Ingrese el numero de terminal GPIO")
#pin = int(raw_input())
pin = 21
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, GPIO.HIGH)
time.sleep(5)
GPIO.output(pin, GPIO.LOW)
GPIO.cleanup(pin)
