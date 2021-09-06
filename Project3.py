import cv2

plate_cascade = cv2.CascadeClassifier("Resources\haarcascades\haarcascade_russian_plate_number.xml")
min_area = 1
vd = cv2.VideoCapture("Resources\plate.mp4")
color = (255,0,255)
count = 0
while True:
    success,img = vd.read()
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = plate_cascade.detectMultiScale(gray_img,1.1,4)
    for (x,y,w,h) in faces:
        area = w*h
        if area > min_area:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(img,"Number Plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            
            img_Roi = img[y:y+h,x:x+w]
            cv2.imshow("ROI", img_Roi)
            
    cv2.imshow("Output",img)
    if cv2.waitKey(1) & 0xFF == ord("x"):
        break
    elif cv2.waitKey(1) & 0xFF == ord("s"):
        cv2.imwrite("Resources/Scanned/NoPlate_"+str(count)+".jpg",img_Roi)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan Saved",(150,265),cv2.FONT_HERSHEY_DUPLEX,
        2,(0,0,255),2)
        cv2.imshow("Result",img)
        cv2.waitKey(500)
        count +=1