from time import sleep
from gpiozero import LightSensor
laserA = LightSensor(4)
laserB = LightSensor(17)
#laserA.wait_for_dark()
#print("Darkness detected")
while True:
	sleep(0.1)
	#print "laserA: %d laserB: %d" % (laserA.value, laserB.value)
	print(laserA.value)
