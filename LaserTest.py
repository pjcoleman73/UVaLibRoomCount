from time import sleep
from gpiozero import LightSensor
laserA = LightSensor(4)
laserB = LightSensor(17)
def laserAtripped():
    atime = time.time()

def laserBtripped():
    btime = time.time()

laserA.when_dark = laserAtripped
laserB.when_dark = laserBtripped

if atime and btime
    v = atime - btime
if v < 0
    add to database
else
    subtract from database
