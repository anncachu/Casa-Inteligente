from sys import argv
import time as tiempo
import RPi.GPIO as GPIO
from sys import exit
GPIO.setmode(GPIO.BCM)

bit3 = 5
bit2 = 11
bit1 = 9
bit0 = 10

GPIO.setup(bit3, GPIO.OUT)
GPIO.setup(bit2, GPIO.OUT)
GPIO.setup(bit1, GPIO.OUT)
GPIO.setup(bit0, GPIO.OUT)

i, bandera, nuevo = -1, 0, 's'
numero = 0
lista = [False, False, False, False]

def salida ():
    if (lista[3] is True):
        GPIO.output(bit3, GPIO.HIGH)
    else:
        GPIO.output(bit3, GPIO.LOW)
    if (lista[2] is True):
        GPIO.output(bit2, GPIO.HIGH)
    else:
        GPIO.output(bit2, GPIO.LOW)
    if (lista[1] is True):
        GPIO.output(bit1, GPIO.HIGH)
    else:
        GPIO.output(bit1, GPIO.LOW)
    if (lista[0] is True):
        GPIO.output(bit0, GPIO.HIGH)
    else:
        GPIO.output(bit0, GPIO.LOW)	

index = open('grados.txt','r')
bandera = int(index.read())
pasos = int(argv[1])
grados = (pasos * 2048) / 360
if (grados >= 2048):
	grados %= 2048
if ((grados - bandera) > 1024):
	bandera += 2048
if ((bandera - grados) > 1024):
	bandera -= 2048
if (bandera < grados):
	while (bandera < grados):
		i += 1
		lista[i % 4] = True
		print (lista)
		salida()
		tiempo.sleep(.01)
		lista[i % 4] = False
		salida()
		bandera += 1
		

if (bandera > grados):
	while (bandera > grados):
		i -= 1
		lista[i % 4] = True
		print (lista)
		salida()
		tiempo.sleep(.01)
		lista[i % 4] = False
		salida()
		if (i < 0):
			i = 3
		bandera -= 1
		
print(lista)
numero = round((bandera * 360) / 2048)
log = open('frame2.html', 'a')
log.write('<br> Camara girada a grado ' + str(numero))
log.close()
index.close()
index = open('grados.txt','w')
index.write(str(bandera))

GPIO.cleanup(bit3)
GPIO.cleanup(bit2)
GPIO.cleanup(bit1)
GPIO.cleanup(bit0)
index.close()
