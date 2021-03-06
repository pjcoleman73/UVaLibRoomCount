# import the necessary packages
from imutils.video import VideoStream
import argparse
import imutils
import time
import cv2
import numpy as np
import Person

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--picamera", type=int, default=-1,
    help="whether or not the Raspberry Pi camera should be used")
args = vars(ap.parse_args())


cnt_up   = 0
cnt_down = 0

cap = cv2.VideoCapture('test.avi') #Open video file
#cap = cv2.VideoCapture(1) #Open video file
#cap = VideoStream(usePiCamera=args["picamera"] > 0).start()
time.sleep(2.0)

#for i in range(19):
#    print(i, cap.get(i))
#
#w = cap.get(3)
#h = cap.get(4)
w = 1280
h = 700
frameArea = h*w
#areaTH = frameArea/250
areaTH = 3700
print('Area Threshold', areaTH)

line_up = int(2*(h/5))
line_down   = int(3*(h/5))
up_limit =   int(1*(h/5))
down_limit = int(4*(h/5))

print("Red line y:",str(line_down))
print("Blue line y:", str(line_up))
line_down_color = (255,0,0)
line_up_color = (0,0,255)
pt1 =  [0, line_down];
pt2 =  [w, line_down];
pts_L1 = np.array([pt1,pt2], np.int32)
pts_L1 = pts_L1.reshape((-1,1,2))
pt3 =  [0, line_up];
pt4 =  [w, line_up];
pts_L2 = np.array([pt3,pt4], np.int32)
pts_L2 = pts_L2.reshape((-1,1,2))

pt5 =  [0, up_limit];
pt6 =  [w, up_limit];
pts_L3 = np.array([pt5,pt6], np.int32)
pts_L3 = pts_L3.reshape((-1,1,2))
pt7 =  [0, down_limit];
pt8 =  [w, down_limit];
pts_L4 = np.array([pt7,pt8], np.int32)
pts_L4 = pts_L4.reshape((-1,1,2))

#fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows = False) #Create the background substractor
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg = cv2.createBackgroundSubtractorGMG() #Create the background substractor

kernelOp = np.ones((3,3),np.uint8)
kernelCl = np.ones((11,11),np.uint8)

#Variables
font = cv2.FONT_HERSHEY_SIMPLEX
persons = []
max_p_age = 5
pid = 1

# Start the frame count
frame_count = 0
while True:
    _,frame = cap.read() #read a frame
    
    for i in persons:
        i.age_one() #age every person one frame

    fgmask = fgbg.apply(frame) #Use the substractor
    fgmask2 = fgbg.apply(frame) #Use the substractor
    
    try:        
        ret,imBin = cv2.threshold(fgmask,200,255,cv2.THRESH_BINARY)
        mask = cv2.morphologyEx(imBin, cv2.MORPH_OPEN, kernelOp)
        mask = cv2.morphologyEx(mask , cv2.MORPH_CLOSE, kernelCl)

        ret,imBin2 = cv2.threshold(fgmask,200,255,cv2.THRESH_BINARY)
        mask2 = cv2.morphologyEx(imBin, cv2.MORPH_OPEN, kernelOp)
        mask2 = cv2.morphologyEx(mask , cv2.MORPH_CLOSE, kernelCl)

#        thresh1 = cv2.threshold(fgmask,200,255,cv2.THRESH_BINARY)
#        opening = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel)
#        cv2.imshow('Background Substraction',opening)

        #cv2.imshow('Frame',frame)
        #cv2.imshow('Background Substraction',fgmask)

    except:
        #if there are no more frames to show...
        print('EOF')
        print('UP:',cnt_up)
        print('DOWN:',cnt_down)
        break
    
    _, contours0, hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours0:
        cv2.drawContours(frame, cnt, -1, (0,255,0), 3, 8)
        area = cv2.contourArea(cnt)
        #if area > areaTH:
        if cv2.contourArea(cnt) > areaTH:
            #################
            #   TRACKING    #
            #################            
            M = cv2.moments(cnt)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            x,y,w,h = cv2.boundingRect(cnt)

            new = True
            if cy in range(up_limit,down_limit):
                for i in persons:
                    if abs(cx-i.getX()) <=w and abs(cy-i.getY()) <= h:
                        
                        new = False
                        i.updateCoords(cx,cy)
                        if i.going_UP(line_down,line_up) == True:
                            cnt_up += 1;
                            print("ID:",i.getId(),'crossed going up at',time.strftime("%c"))
                        elif i.going_DOWN(line_down,line_up) == True:
                            cnt_down += 1;
                            print("ID:",i.getId(),'crossed going down at',time.strftime("%c"))
                        break
                    if i.getState() == '1':
                        if i.getDir() == 'down' and i.getY() > down_limit:
                            i.setDone()
                        elif i.getDir() == 'up' and i.getY() < up_limit:
                            i.setDone()
                    if i.timedOut():
                        #sacar i de la lista persons
                        index = persons.index(i)
                        persons.pop(index)
                        del i
                        break
                if new == True:
                    p = Person.MyPerson(pid,cx,cy, max_p_age)
                    persons.append(p)
                    pid += 1
            cv2.circle(frame,(cx,cy), 5, (0,0,255), -1)
            img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            #cv2.drawContours(frame, cnt, -1, (0,255,0), 3)
            
    for i in persons:
#        if len(i.getTracks()) >= 2:
#            pts = np.array(i.getTracks(), np.int32)
#            pts = pts.reshape((-1,1,2))
#            frame = cv2.polylines(frame,[pts],False,i.getRGB())
#        if i.getId() == 9:
#            print(str(i.getX()), ',', str(i.getY()))
        cv2.putText(frame, str(i.getId()),(i.getX(),i.getY()),font,0.3,i.getRGB(),1,cv2.LINE_AA)
        
    # increment the frame count
    frame_count += 1
    # Reset the up and down counts to 0 for the first 100 frames to get rid of
    # false positives during start up
    if frame_count < 100:
        cnt_up = 0
        cnt_down = 0

    str_up = 'UP: '+ str(cnt_up)
    str_down = 'DOWN: '+ str(cnt_down)
    frame = cv2.polylines(frame,[pts_L1],False,line_down_color,thickness=2)
    frame = cv2.polylines(frame,[pts_L2],False,line_up_color,thickness=2)
    frame = cv2.polylines(frame,[pts_L3],False,(255,255,255),thickness=1)
    frame = cv2.polylines(frame,[pts_L4],False,(255,255,255),thickness=1)
    cv2.putText(frame, str_up ,(10,40),font,0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame, str_up ,(10,40),font,0.5,(0,0,255),1,cv2.LINE_AA)
    cv2.putText(frame, str_down ,(10,90),font,0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame, str_down ,(10,90),font,0.5,(255,0,0),1,cv2.LINE_AA)

            
    cv2.imshow('Frame',frame)
    #Abort and exit with 'Q' or ESC
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release() #release video file
cv2.destroyAllWindows() #close all openCV windows
