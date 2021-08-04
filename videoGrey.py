import cv2
import numpy as np 
# 0 is for camera 1(if there are multiple cameras)
vid = cv2.VideoCapture(0)

while(True):
    ret,frame = vid.read()
    #captures the video frame by frame 
    #ret Returns True if it captures correctly 

    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #Display the resulting frame 
    cv2.imshow('Grey Frame',grey)
    #cv2.imwrite('pick.jpeg',frame)

    #The'q' button is set as quitting button 
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()


