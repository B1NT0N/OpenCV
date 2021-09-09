import pytesseract
import cv2
from pytesseract import Output

img = cv2.imread("Resources\cards.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\\tesseract.exe"
image_data = pytesseract.image_to_data(img, output_type=Output.DICT)


print(pytesseract.image_to_string(img))

for i, word in enumerate(image_data['text']):
	if word != '':
		x,y,w,h = image_data['left'][i],image_data['top'][i],image_data['width'][i],image_data['height'][i]
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)
		cv2.putText(img,word,(x,y-16),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)

cv2.imshow("Image",img)
cv2.waitKey(0)




