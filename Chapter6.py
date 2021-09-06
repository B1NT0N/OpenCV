import cv2
import numpy as np
from numpy.core.shape_base import hstack


img = cv2.imread("Resources\kali-menu.png")

#Horizontal Stack
horizontal_stack = np.hstack((img, img))
cv2.imshow("Output",horizontal_stack)
#Vertical Stack
vertical_stack = np.vstack((img, img))
cv2.imshow("Output",vertical_stack)


cv2.waitKey(0)