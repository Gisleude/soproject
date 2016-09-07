import Adafruit_BBIO.GPIO as GPIO
import time
import sys

GPIO.setup("P9_14", GPIO.OUT)
GPIO.setup("P9_12", GPIO.OUT)
GPIO.setup("P9_16", GPIO.OUT)
GPIO.setup("P9_27", GPIO.IN)

i = 0

while True:
	#POTENCIOMETRO
	potenciometro = open("/sys/bus/iio/devices/iio:device0/in_voltage1_raw","r+") 
	string_p = potenciometro.read()
	valor = int(string_p)
	v = (valor*1.8)/4096
  	
	#FOTORESISTOR
	foto = open("/sys/bus/iio/devices/iio:device0/in_voltage3_raw","r+")
	string_f = foto.read()
	valor = int(string_f)
	omh = (valor*10000)/4096	

	if omh <= 70:
		i = 1
	
	elif omh > 70:
		i = 0

	if GPIO.input("P9_27") == True and i == 0:
		i = 1
		time.sleep(0.2)
	elif GPIO.input("P9_27") == True and i == 1:
		i = 0
		time.sleep(0.2)
	if i == 0:
		#Verde
		GPIO.output("P9_14",0)
		#Vermelho
		GPIO.output("P9_12",0)
		#Azul
		GPIO.output("P9_16",0)
	elif i == 1:
		if v <= 0.8 : 
			GPIO.output("P9_14",1)
			GPIO.output("P9_12",0)
			GPIO.output("P9_16",0)
		elif v > 0.8 and v <= 1.5:
			GPIO.output("P9_16",1)
			GPIO.output("P9_12",0)
			GPIO.output("P9_14",0)
		elif v > 1.5:
			GPIO.output("P9_12",1)
			GPIO.output("P9_14",0)
			GPIO.output("P9_16",0)
	print omh
	
file.close()
