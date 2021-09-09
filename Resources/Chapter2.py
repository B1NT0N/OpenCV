import cv2
import numpy as np

kernel= np.ones((5,5),np.uint8)
img = cv2.imread("Resources\example.png")

#Grayscaled Image
""" Grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Output",Grayimg) """

#Blured Image
""" Blurimg = cv2.GaussianBlur(img, (15,15),0)
cv2.imshow("Output",Blurimg) """

#Edge Detection
""" edge_img = cv2.Canny(img,100,100)
    #Dialation
dialation_img = cv2.dilate(edge_img,kernel,1)
cv2.imshow("Output",dialation_img) """

#Eroted Image
""" Eroted_img = cv2.erode(img,kernel,iterations=2)
cv2.imshow("Output",Eroted_img) """

cv2.waitKey(0)