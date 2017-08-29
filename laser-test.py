from time import sleep
from gpiozero import LaserSensor

ldr = LaserSensor(4)

while True:
    sleep(2)
    print(ldr.value)
