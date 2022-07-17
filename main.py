import cv2 as cv
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv.imread('img.png')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# print(pytesseract.image_to_string(img))

### Detecting Characters
hImg, wImg,_ = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    print(b)
    b = b.split(' ')
    print(b)
    x,y,w,h = int(b[1]), int(b[2]), int(b[3]), int(b[4])

cv.imshow('Result', img)
cv.waitKey(0)
