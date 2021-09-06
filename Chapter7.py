import cv2
import numpy as np

def empty(value):
    pass

cv2.namedWindow("TrackBar")
cv2.resizeWindow("TrackBar",640,240)
cv2.createTrackbar("heu_min","TrackBar",0,179,empty)
cv2.createTrackbar("heu_max","TrackBar",19,179,empty)
cv2.createTrackbar("sat_min","TrackBar",110,255,empty)
cv2.createTrackbar("sat_max","TrackBar",255,255,empty)
cv2.createTrackbar("val_min","TrackBar",123,255,empty)
cv2.createTrackbar("val_max","TrackBar",255,255,empty)

while True:
    img = cv2.imread("Resources\lambo.png")
    img_HSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("heu_min","TrackBar")
    h_max = cv2.getTrackbarPos("heu_max","TrackBar")
    s_min = cv2.getTrackbarPos("sat_min","TrackBar")
    s_max = cv2.getTrackbarPos("sat_max","TrackBar")
    v_min = cv2.getTrackbarPos("val_min","TrackBar")
    v_max = cv2.getTrackbarPos("val_max","TrackBar")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    
    mask = cv2.inRange(img_HSV,lower,upper)
    img_result = cv2.bitwise_and(img,img,mask=mask)
    
    cv2.imshow("Result",img_result)
    cv2.imshow("Output",img)
    #cv2.imshow("HSV",img_HSV)

    cv2.waitKey(1)