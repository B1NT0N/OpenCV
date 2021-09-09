import cv2
import numpy as np

width_img=360
height_img =480

vd = cv2.VideoCapture(0)
vd.set(10,150)

def preprocessing(img):
    gray_img =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur_img = cv2.GaussianBlur(gray_img,(5,5),1)
    canny_img = cv2.Canny(blur_img,200,200)
    kernel = np.ones((5,5))
    dialation_img = cv2.dilate(canny_img,kernel,iterations=2)
    threshold_img = cv2.erode(dialation_img,kernel,iterations=1)
    
    return threshold_img

def get_contours(img):
    biggest = np.array([])
    maxArea = 0
    contours,hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area =cv2.contourArea(cnt)
        if area > 5000:
            cv2.drawContours(contour_img,cnt,-1,(255,255,0),2)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
    cv2.drawContours(contour_img,biggest,-1,(255,255,0),10)
    return biggest

def get_warp(img,biggest):
    biggest = reorder(biggest)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [width_img, 0], [0, height_img], [width_img, height_img]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    output_img = cv2.warpPerspective(img, matrix, (width_img, height_img))
    
    crop_img = output_img[20:output_img.shape[0]-20,20:output_img.shape[1]-20]
    crop_img = cv2.resize(crop_img,(width_img,height_img))

    return output_img

def reorder(my_points):
    my_points = my_points.reshape((4,2))
    my_new_points = np.zeros((4,1,2),np.int32)
    add = my_points.sum(1)
    my_new_points[0] = my_points[np.argmin(add)]
    my_new_points[3] = my_points[np.argmax(add)]
    diff = np.diff(my_points,axis=1)
    my_new_points[1]= my_points[np.argmin(diff)]
    my_new_points[2] = my_points[np.argmax(diff)]
    
    return my_new_points

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

while True:
    success, img = vd.read()
    #img = cv2.imread("Resources\document.jpg") #static img
    img = cv2.resize(img,(width_img,height_img))
    contour_img = img.copy()
    threshold_img = preprocessing(img)
    
    biggest = get_contours(threshold_img)
    
    if biggest.size !=0:
        warp_img = get_warp(img,biggest) 
        array_img = ([img,threshold_img],
                    [contour_img,warp_img])
    else:
        array_img = ([img,threshold_img],
                    [contour_img,img])
    
    stack_img = stackImages(0.6,array_img)
    
    cv2.imshow("Result" ,stack_img)
    
    if cv2.waitKey(1) & 0xFF == ord("x"):
        break