from time import sleep
from gpiozero import LightSensor
ldr = LightSensor(4)
lazer2 = LightSensor(17)
while True:
	sleep(0.1)
	if ldr.value < 0.5:
		print(ldr.value)
