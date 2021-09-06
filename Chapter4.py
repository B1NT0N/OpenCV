import cv2
import numpy as np

img = np.zeros((512,512),np.uint8)

#Creating a line
cv2.line(img,(0,0),(250,250),(255,255,255),2)
#Creating a rectangle
cv2.rectangle(img,(0,0),(250,250),(255,255,255),2)
#Creating a circle
cv2.circle(img,(125,125),125,(255,255,255),2)
#Creating a OnScrrenText
cv2.putText(img,"Hello World",(125,125),cv2.FONT_HERSHEY_PLAIN,1,(255,255,255))

cv2.imshow("Output", img)
cv2.waitKey(0)