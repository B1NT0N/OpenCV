import cv2

#Open Images
""" img = cv2.imread("Resources\example.png")
cv2.imshow("Output",img)
cv2.waitKey(0) """


#Open Videos
""" vd = cv2.VideoCapture("Resources\example_video.mp4")
while True:
    success,img = vd.read()
    cv2.imshow("Output",img)
    if cv2.waitKey(1) & 0xFF == ord("x"):
        break """
        
#Open Webcam
""" vd = cv2.VideoCapture(0)
vd.set(3,640)
vd.set(4,480)
vd.set(10,100)

while True:
    success,img = vd.read()
    cv2.imshow("Output",img)
    if cv2.waitKey(1) & 0xFF == ord("x"):
        break """