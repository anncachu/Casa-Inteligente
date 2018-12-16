from sys import argv
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)             
GPIO.setmode(GPIO.BCM)

pin =  11
  
GPIO.setup(pin,GPIO.OUT)    
Salida = GPIO.PWM(pin,50)        
Salida.start(0)

grados = int(argv[1])
invgrados = (grados - 180) * (-1)
cgrados = ((0.5 + ((invgrados * 2) / 180)) * 12.5) / 2.5
while(cgrados < 2.5 or cgrados > 12.5):
	print("Valor invalido")
	grados = int(input('Grados: '))
	cgrados = ((0.5 + ((invgrados * 2) / 180)) * 12.5) / 2.5
Salida.ChangeDutyCycle(cgrados)
time.sleep(1)
log = open('frame2.html', 'a')
log.write('<br> Cortina 2 a grado ' + str(grados))
log.close()
#Salida.stop()
#GPIO.cleanup(21)

