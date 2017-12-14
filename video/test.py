import numpy as np
import cv2

cap = cv2.VideoCapture('peopleCounter.avi')

width = cap.get(3)
height = cap.get(4)

midx = int(width/2)
midy = int(height/2)

count = 0

while(cap.isOpened()):
    ret, frame = cap.read()
    try:
        count = count + 1
        text = 'Count at: ' + str(count)
        cv2.putText(frame, text, (midx, midy), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
        cv2.imshow('Frame', frame)

        sampleFrame = frame
    except:
        print('EOF')
        break

    line1 = np.array([[100,100], [300,100], [350,300]], np.int32).reshape((-1,1,2))
    line2 = np.array([[400,50], [450,300]], np.int32).reshape((-1,1,2))

    sampleFrame = cv2.polylines(sampleFrame, [line1], False, (255,0,0), thickness=2)
    sampleFrame = cv2.polylines(sampleFrame, [line2], False, (0,0,255), thickness=4)

    cv2.imshow('Sample Frame', sampleFrame)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
