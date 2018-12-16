from sys import argv
import time as tiempo
import RPi.GPIO as GPIO
from sys import exit
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

acttxt = open('act.txt','w')

if (argv[1] == '1'):
	acttxt.write('1')	
	
elif (argv[1] == '2'):
	acttxt.write('2')
	
elif (argv[1] == '3'):
	acttxt.write('3')
	
elif (argv[1] == '4'):
	acttxt.write('4')
	
elif (argv[1] == '5'):
	acttxt.write('5')
	
elif (argv[1] == '6'):
	acttxt.write('6')
	
elif (argv[1] == '7'):
	acttxt.write('7')
	
elif (argv[1] == '8'):
	acttxt.write('8')
	
acttxt.close()
