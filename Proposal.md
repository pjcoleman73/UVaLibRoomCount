# UVa Library Room Counter Proposal
We propose to build a people counter from a Raspberry Pi. When complete the device will detect the number of people entering a space, exiting a space, display the current net total of the space, and record the data over a set period of time.  
After system is tested and operational, we will conduct an evaluation over the course of 1 month. This evaluation  will be in the Alderman's Current Journals Room due to its single entrance/exit. The evaluation should involve live counts and match them to the system's automated count to determine accuracy.
Final proposal should include timeline for testing, evaluation, and rollout to other libraries.

NOTE: This may already exist, but I don’t know my way around Github to know for sure.
http://measurethefuture.net
https://github.com/MeasureTheFuture

## Stage I
Build Raspberry Pi people counter.
Keep running tally for people entering and exiting a given room.
Next Stages (not sure the logical order)
Separate data by 24 hour periods.
Send data continuously to networked database for record keeping.
If room has two or more access points, each with their own counter, can the system calculate a live room count based on the data coming from various counters?
Display live data from single and/or multiple rooms on a webpage or series of linked webpages.
Allow patrons to see live room volume vs. capacity on a monitor at building entrance. Give patrons ability to choose study space based on current room capacity.
Install room capacity information kiosks at entrance to each room.
LOCATIONS (Alderman, to start)   (most rooms will need counters above each entrance/exit and ability to cross-reference each live tally into a live composite number)
Reference Room (4th Flr)
minus Ref. Office, Circ Office, Kurt's Office.
Scholars' Lab (4th Flr)
minus 421, 423, stairs, elevator
cannot account for Makerspace.
Current Journals Rm (3rd Flr)**PILOT LOCATION
Map Rm (3rd Flr)
minus Grad Reading Room.
McGregor Rm (2nd Flr)
minus Asian Studies Rm.
Asian Studies Rm (2nd Rm)
include newspaper room.
minus McGregor Rm and Library Offices.
RESOURCES
http://www.pyimagesearch.com/2015/05/25/basic-motion-detection-and-tracking-with-python-and-opencv/
https://spruce.me/blogs/technology/114408580-how-many-people-walk-by-the-shop-every-day-an-exercise-in-computer-vision
https://github.com/donce71/Pedestrians-counter-raspberry
EQUIPMENT NEEDED
Raspberry Pi 3 - $35
32 GB Micro SD Card (Class 10) - $13
To start, but smaller size may be all we need.
2.5A USB Power Supply with Micro USB Cable - $8
Case -
Would be nice, but not necessary for development & testing. Could 3D print something basic & functional.
HDMI (male-to-male) cable - $1
Raspberry Pi-compatible camera
Raspberry Pi Camera Module V2 - 8 Megapixel, 1080p - $29
https://www.amazon.com/Raspberry-Pi-Camera-Module-Megapixel/dp/B01ER2SKFS/
Arducam OV5647 - 5 Megapixels 1080p - $15
https://www.amazon.com/Arducam-Megapixels-Sensor-OV5647-Raspberry/dp/B012V1HEP4/
QUESTIONS
Can the data be sent to LibAnalytics?
Data from front door counter, if eventually installed.
Could this be created, coded, and saved as an image so anyone can build the hardware, load the software, and configure for their own use?
Can this be done with the Raspberry Pi Zero r an Arduino? It would be cheaper, but might be underpowered. Develop and test with the Raspberry Pi 3, then make determination.
Raspberry Pi 3 ($35)
1.2 GHz 64-bit quad-core ARMv8 CPU
1 GB of RAM
Raspberry Pi Zero W ($10)
1 GHz single-core CPU
512 MB of RAM

NEXT STEPS
Discuss with Ammon Shepherd from Scholars' Lab.
Which tactic is most feasible?
Timeline?
Can we bust out a prototype in a 1-day "hack-a-thon"?
