import cv2
import numpy as np

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def get_contours(img):
    contours,hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area =cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(cnt_img,cnt,-1,(255,0,255),2)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            obj_coord = len(approx)
            x,y,w,h = cv2.boundingRect(approx)
            
            if obj_coord == 3:object_type="Triangle"
            elif obj_coord == 4:object_type="square"
            elif obj_coord > 4:object_type="Cirlcle?"
            else :object_type="Line?"
            
            cv2.rectangle(cnt_img,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(cnt_img,object_type,(x+int(w/2),y+int(h/2)),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
            
#Open Images
img = cv2.imread("Resources\shapes.png")
cnt_img = img.copy()
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur_img = cv2.GaussianBlur(gray_img,(7,7),1)
canny_img = cv2.Canny(blur_img,50,50)
get_contours(canny_img)

empty_img = np.zeros_like(img)
img_stack = stackImages(0.2,([img,gray_img,blur_img],[canny_img,cnt_img,empty_img]))

cv2.imshow("Output",img_stack)
cv2.waitKey(0)