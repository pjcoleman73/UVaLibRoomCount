# Diagram of trip wires A and B

```
           The Room
_                            __
D |                       B{| D
O |                         | O  
O |                         | O
R |                       A{| R
--                          --

        Out of the Room


  IN =>     A       ->       B
         14:30:27    -    14:30:30   =  (negative)

            A       <-       B
 OUT <=  12:22:22    -    12:22:20   =  (positive)
```


# Hardware Needed

* Photo reistors
* Capacitors
* Lasers
    * https://www.amazon.com/GeeBat-10pcs-Laser-Module-Lasers/dp/B01ITK4PEO/ref=sr_1_1?ie=UTF8&qid=1495547486&sr=8-1&keywords=laser+diode
* Raspberry Pi Zero W

# Tutorials
* GPIO pins: https://www.raspberrypi.org/documentation/usage/gpio-plus-and-raspi2/
* Photo resistor
  * https://www.raspberrypi.org/learning/laser-tripwire/worksheet/
* Laser
  * http://www.instructables.com/id/Raspberry-Pi-Laser-Security-System/
  * https://www.youtube.com/watch?v=pO1dTkLrod8

# Sudo code
## Sudo code for single trip wire

```
from gpiozero import LightSensor
from time import sleep

ldr = LightSensor(4)  # alter if using a different pin

while True:
    sleep(0.1)
    if ldr.value < 0.5:  # adjust this to make the circuit more or less sensitive
        # send value to database

```


## Sudo code for two trip wires

```
from gpiozero import LightSensor 
from time import sleep, time

lzrA = LightSensor(4)  # alter number if using a different pin
lzrB = LightSensor(7)  # alter number if using a different pin

def lzrAtrip():
    aTime = time.time()

def lzrBtrip():
    bTime = time.time()

lzrA.when_dark = lzrAtrip
lzrB.when_dark = lzrBtrip

if aTime and bTime:
    V = aTime - bTime

    if V < 0:
      # add 1 to database
    else:
      # subtract 1 from database
      

```

