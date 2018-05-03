# UVaLibRoomCount
The purpose of this project is to develop an anonymized, low-cost, networked tool for providing a live count of people in a study space at any given time. The purpose is to allow students to waste less time finding a study space with empty seats around Grounds and more time actually studying. 

# CURRENT STATUS
This project is not the primary (or even secondary) job function for either Ammon or PJ, but we are both interested in making it a reality. With not much time to dedicate, progress has been slow. 
We began by experimenting with using lasers and photo resistors to create two "laser trip wires" working in tandum to determine whether a specific object had entered or exited a given threshold. 
We moved on to experimenting with OpenCV in Python using a webcam to input the visual data. We have followed multiple tutorials and have encoutered numerous problems with each. 

The most recent files are in the 'video' folder. These files play around with different options in attempt to solve the following issues we had (they are unresolved):
- false counting at the beginning of the script running
- two people walking abreast are seen as one object rather than two
- false positive counts, and untracked counts.

# Tutorials

- Install openCV on Raspberry Pi Zero W
  - https://www.pyimagesearch.com/2015/12/14/installing-opencv-on-your-raspberry-pi-zero/
  - Installed using python 3 rather than 2.7
- PiCamera and OpenCV
  - https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/
