import cv2
import numpy as np

kernel= np.ones((5,5),np.uint8)
img = cv2.imread("Resources\example.png")

#print(img.shape) #show image size

#resize Image
""" img_resize = cv2.resize(img,(640,640))
cv2.imshow("Output",img_resize)
 """
#Crop image
""" img_crop = img[0:512,0:512]
cv2.imshow("Output",img_crop) """
cv2.waitKey(0)