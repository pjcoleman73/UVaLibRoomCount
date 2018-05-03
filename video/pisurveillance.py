# https://www.pyimagesearch.com/2015/06/01/home-surveillance-and-motion-detection-with-the-raspberry-pi-python-and-opencv/
# https://www.pyimagesearch.com/2016/01/04/unifying-picamera-and-cv2-videocapture-into-a-single-class-with-opencv/
# import the necessary packages
from imutils.video import VideoStream
import argparse
import datetime
import imutils
import time
import cv2
 
DELTATHRESH = 5
MINAREA = 9000
FRAMEWIDTH = 400

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--picamera", type=int, default=-1, help="whether or not the Raspberry Pi camera should be used")
args = vars(ap.parse_args())

# initialize the video stream and allow the cammera sensor to warmup
#vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
cap = cv2.VideoCapture('AVItest.avi')
# add bgsegm to get it to work
# https://stackoverflow.com/questions/18721552/opencv2-python-createbackgroundsubtractor-module-not-found
#fgbg = cv2.createBackgroundSubtractorMOG2(varThreshold = 8, detectShadows = False)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

 
# allow the camera to warmup, then initialize the average frame, last
# uploaded timestamp, and frame motion counter
print("[INFO] warming up...")
avg = None

# capture frames from the camera
#for f in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
while True:
    _, frame = cap.read()
    # frame = vs.read()
    timestamp = datetime.datetime.now()
    #cv2.imshow("Original Image", frame)


    # resize the frame, convert it to grayscale, and blur it
    #frame = imutils.resize(frame, width=FRAMEWIDTH)
    #height = frame.shape[0]
    #width = frame.shape[1]
    line1Height = int(height/2.5)
    line2Height = int(height/1.2)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
 
    # apply the background subtractor (which converts to black and white)
    #gray = fgbg.apply(frame)

    # if the average frame is None, initialize it
    if avg is None:
        print("[INFO] starting background model...")
        avg = gray.copy().astype("float")
        continue

    # accumulate the weighted average between the current frame and
    # previous frames, then compute the difference between the current
    # frame and running average
    cv2.accumulateWeighted(gray, avg, 0.5)
    frameDelta = cv2.absdiff(gray, cv2.convertScaleAbs(avg))

    # threshold the delta image, dilate the thresholded image to fill
    # in holes, then find contours on thresholded image
    thresh = cv2.threshold(frameDelta, DELTATHRESH, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow("", thresh)
    thresh = cv2.dilate(thresh, None, iterations=8)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]

    # loop over the contours
    for c in cnts:
        # if the contour is too small, ignore it
        if cv2.contourArea(c) < MINAREA:
            continue

        # compute the center of the object
        M = cv2.moments(c)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

        # draw the contour
        cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
        # draw the center
        cv2.circle(frame, (cX,cY), 7, (0,0,255), -1)
        # compute the bounding box for the contour, draw it on the frame,
        # and update the text
        #(x, y, w, h) = cv2.boundingRect(c)
        #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # draw the text and timestamp on the frame
    ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
    cv2.putText(frame, ts, (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
    cv2.line(frame, (0,line1Height), (width,line1Height), (255, 0, 0), 4)
    cv2.line(frame, (0,line2Height), (width,line2Height), (0, 255, 0), 4)
    #cv2.putText(frame,'People Going Above = '+str(crossedAbove),(100,50), font, 1,(255,255,255),2,cv2.LINE_AA)
    #cv2.putText(frame,'People Going Below = '+str(crossedBelow),(100,100), font, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.imshow("Room Count", frame)
    key = cv2.waitKey(1)

    # if the `q` key is pressed, break from the lop
    if key == ord("q"):
        break

cv2.destroyAllWindows()
