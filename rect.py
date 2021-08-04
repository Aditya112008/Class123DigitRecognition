import numpy as np
import cv2

#numpy.ones reshapes the array--width600,height 800
rect=np.ones((600,800,3),dtype=np.uint8)*255

#bgr--red color below one
#10 is the thickness
cv2.rectangle(rect,(0,int(600/2)),(int(800/2),599),(255,0,0),20)
cv2.imshow("image",rect)
cv2.waitKey()
cv2.destroyAllWindows()

#bgr below in green
#-1 so no border
cv2.rectangle(rect,(int(800/2),0),(799,int(600/2)),(0,255,0),-1)
cv2.imshow("image",rect)
cv2.waitKey()
cv2.destroyAllWindows()
