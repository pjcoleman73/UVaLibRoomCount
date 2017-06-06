# Diagram of trip wires A and B

```
  A    -   B
  2    -   1  <-  = positive OUT
  1    -   2  ->  = negative IN
```


# Hardware Needed

* Photo reistors
* Capacitors
* Lasers
    * https://www.amazon.com/GeeBat-10pcs-Laser-Module-Lasers/dp/B01ITK4PEO/ref=sr_1_1?ie=UTF8&qid=1495547486&sr=8-1&keywords=laser+diode
* Raspberry Pi Zero W

# Tutorials
* GPIO pins: https://www.raspberrypi.org/documentation/usage/gpio-plus-and-raspi2/
* https://www.raspberrypi.org/learning/laser-tripwire/worksheet/

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

ldrA = LightSensor(4)  # alter if using a different pin
ldrB = LightSensor(7)  # alter if using a different pin

while True:
    sleep(0.1)
    if ldrA.value < 0.5:  # adjust this to make the circuit more or less sensitive
        Atime = time.time() * 1000 # to get miliseconds
    if ldrB.value < 0.5:
        Btime = time.time() * 1000
    V = Atime - Btime
    if V is negative then IN, else OUT

```

