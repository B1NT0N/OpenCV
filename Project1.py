import cv2
import numpy as np

frameWidth = 480
frameHeight = 360

vd = cv2.VideoCapture(0)
vd.set(3, frameWidth)
vd.set(4, frameHeight)
vd.set(10,150)

my_colors = [
            [140,110,0,179,255,255],
            [46,93,0,83,255,255],
            [88,150,83,123,255,255]
            ]

my_color_value = [[0,0,255],
                [0,255,0],
                [255,0,0],
]

my_points = []

def color_finder(img,my_colors):
    img_HSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    new_points=[]
    count = 0
    for color in my_colors:
        
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        
        mask = cv2.inRange(img_HSV,lower,upper)
        
        x,y,radius = get_contours(mask)
        cv2.circle(img_result,(x,y),radius,my_color_value[count],cv2.FILLED)
        if x!=0 and y!=0:
            new_points.append([x,y,radius,count])
        count +=1
    return new_points
    
def get_contours(img):
    contours,hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    peri = 1
    for cnt in contours:
        area =cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(img_result,cnt,-1,(255,0,255),2)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h = cv2.boundingRect(approx)
    return x+w//2,y+h//2,int((np.log(peri))*4)

def draw_on_canvas(my_points,my_color_value):
    for point in my_points:
        cv2.circle(img_result,(point[0],point[1]),10,my_color_value[point[3]],cv2.FILLED)
        
while True:
    success, img = vd.read()
    img_result = img.copy()
    new_points = color_finder(img,my_colors)
    if len(new_points)!=0:
        for newP in new_points:
            my_points.append(newP)
    if len(my_points)!=0:
        draw_on_canvas(my_points,my_color_value)
        
    cv2.imshow("Result", img_result)    
    if cv2.waitKey(1) & 0xFF == ord("x"):
        break