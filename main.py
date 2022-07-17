import cv2 as cv
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv.imread('img.png')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# print(pytesseract.image_to_string(img))

### Detecting Characters
hImg, wImg,_ = img.shape
pytesseract.image_to_boxes(img)

cv.imshow('Result', img)
cv.waitKey(0)
