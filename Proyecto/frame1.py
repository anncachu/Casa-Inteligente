from sys import argv
import time as tiempo
import RPi.GPIO as GPIO
from sys import exit
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

foco1 = 22
foco2 = 27
foco3 = 17
foco4 = 4
foco5 = 3
foco6 = 2
foco7 = 23
foco8 = 18

boton1 = 21
boton2 = 20
boton3 = 16
boton4 = 12
boton5 = 7
boton6 = 8
boton7 = 25
boton8 = 24

motora = 26
motorb = 19
motorc = 13
motord = 6

GPIO.setup(foco1, GPIO.OUT)
GPIO.setup(foco2, GPIO.OUT)
GPIO.setup(foco3, GPIO.OUT)
GPIO.setup(foco4, GPIO.OUT)
GPIO.setup(foco5, GPIO.OUT)
GPIO.setup(foco6, GPIO.OUT)
GPIO.setup(foco7, GPIO.OUT)
GPIO.setup(foco8, GPIO.OUT)

GPIO.setup(boton1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(boton2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(boton3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(boton4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(boton5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(boton6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(boton7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(boton8, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(boton1, GPIO.RISING, bouncetime=300)
GPIO.add_event_detect(boton2, GPIO.RISING, bouncetime=300)
GPIO.add_event_detect(boton3, GPIO.RISING, bouncetime=300)
GPIO.add_event_detect(boton4, GPIO.RISING, bouncetime=300)
GPIO.add_event_detect(boton5, GPIO.RISING, bouncetime=300)
GPIO.add_event_detect(boton6, GPIO.RISING, bouncetime=300)
GPIO.add_event_detect(boton7, GPIO.RISING, bouncetime=300)
GPIO.add_event_detect(boton8, GPIO.RISING, bouncetime=300)

def acciona (txt, foco, act, mensaje1, mensaje2):
	focotxt = open(txt,'r')
	
	if (focotxt.read() == '0'):
		log.write(mensaje1)
		GPIO.output(foco, GPIO.HIGH)
		focotxt.close()
		focotxt = open(txt,'w')
		focotxt.write('1')
	else:
		log.write(mensaje2)
		GPIO.output(foco, GPIO.LOW)
		focotxt.close()
		focotxt = open(txt,'w')
		focotxt.write('0')

	focotxt.close()
	act.close()
	act = open('act.txt','w')
	act.write('0')

while(True):
	acttxt = open('act.txt','r')
	log = open('frame2.html', 'a')
	lectura = acttxt.read()	
	if GPIO.event_detected(boton1):
		GPIO.remove_event_detect(boton1)
		acciona('foco1.txt', foco1, acttxt, '<br> foco1 prendido', '<br> foco1 apagado')
		GPIO.add_event_detect(boton1, GPIO.RISING, bouncetime=300)
	elif GPIO.event_detected(boton2):
		GPIO.remove_event_detect(boton2)
		acciona('foco2.txt', foco2, acttxt, '<br> foco2 prendido', '<br> foco2 apagado')
		GPIO.add_event_detect(boton2, GPIO.RISING, bouncetime=300)
	elif GPIO.event_detected(boton3):
		GPIO.remove_event_detect(boton3)
		acciona('foco3.txt', foco3, acttxt, '<br> foco3 prendido', '<br> foco3 apagado')
		GPIO.add_event_detect(boton3, GPIO.RISING, bouncetime=300)
	elif GPIO.event_detected(boton4):
		GPIO.remove_event_detect(boton4)
		acciona('foco4.txt', foco4, acttxt, '<br> foco4 prendido', '<br> foco4 apagado')
		GPIO.add_event_detect(boton4, GPIO.RISING, bouncetime=300)
	elif GPIO.event_detected(boton5):
		GPIO.remove_event_detect(boton5)
		acciona('foco5.txt', foco5, acttxt, '<br> foco5 prendido', '<br> foco5 apagado')
		GPIO.add_event_detect(boton5, GPIO.RISING, bouncetime=300)
	elif GPIO.event_detected(boton6):
		GPIO.remove_event_detect(boton6)
		acciona('foco6.txt', foco6, acttxt, '<br> foco6 prendido', '<br> foco6 apagado')
		GPIO.add_event_detect(boton6, GPIO.RISING, bouncetime=300)
	elif GPIO.event_detected(boton7):
		GPIO.remove_event_detect(boton7)
		acciona('foco7.txt', foco7, acttxt, '<br> foco7 prendido', '<br> foco7 apagado')
		GPIO.add_event_detect(boton7, GPIO.RISING, bouncetime=300)
	elif GPIO.event_detected(boton8):
		GPIO.remove_event_detect(boton8)
		acciona('foco8.txt', foco8, acttxt, '<br> foco8 prendido', '<br> foco8 apagado')
		GPIO.add_event_detect(boton8, GPIO.RISING, bouncetime=300)
	elif(lectura == '1'):
		acciona('foco1.txt', foco1, acttxt, '<br> foco1 prendido', '<br> foco1 apagado')
		
	elif(lectura == '2'):
		acciona('foco2.txt', foco2, acttxt, '<br> foco2 prendido', '<br> foco2 apagado')
		
	elif(lectura == '3'):
		acciona('foco3.txt', foco3, acttxt, '<br> foco3 prendido', '<br> foco3 apagado')
		
	elif(lectura == '4'):
		acciona('foco4.txt', foco4, acttxt, '<br> foco4 prendido', '<br> foco4 apagado')
		
	elif(lectura == '5'):
		acciona('foco5.txt', foco5, acttxt, '<br> foco5 prendido', '<br> foco5 apagado')
		
	elif(lectura == '6'):
		acciona('foco6.txt', foco6, acttxt, '<br> foco6 prendido', '<br> foco6 apagado')
		
	elif(lectura == '7'):
		acciona('foco7.txt', foco7, acttxt, '<br> foco7 prendido', '<br> foco7 apagado')
		
	elif(lectura == '8'):
		acciona('foco8.txt', foco8, acttxt, '<br> foco8 prendido', '<br> foco8 apagado')
		
	acttxt.close()
