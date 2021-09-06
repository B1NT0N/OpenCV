import cv2
import numpy as np
#Perspective Warp
width,height = 250,350

pts1 = np.float32([[int(394/3),int(15/3)],[int(708/3),int(15/3)],[int(369/3),int(386/3)],[int(737/3),int(385/3)]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

img = cv2.imread("Resources\cards.jpg")
img_resize = cv2.resize(img,(int(img.shape[0]/3),int(img.shape[1]/3)))

matrix = cv2.getPerspectiveTransform(pts1,pts2)
img_out = cv2.warpPerspective(img_resize,matrix,(width,height))

cv2.imshow("Image",img_resize)
cv2.imshow("Output",img_out)

cv2.waitKey(0)

