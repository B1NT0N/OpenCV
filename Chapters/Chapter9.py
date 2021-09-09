import cv2

face_cascade = cv2.CascadeClassifier("Resources\haarcascades\haarcascade_righteye_2splits.xml")
#img = cv2.imread("Resources\example.png")


vd = cv2.VideoCapture(0)
vd.set(3,640)
vd.set(4,480)
vd.set(10,100)

while True:
    success,img = vd.read()
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img,1.1,4)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow("Output",img)
    if cv2.waitKey(1) & 0xFF == ord("x"):
        break
