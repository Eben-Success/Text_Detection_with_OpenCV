import cv2
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('toi.jpg', cv2.COLOR_BGR2GRAY)
print(pytesseract.image_to_string(img))
cv2.imshow('Result', img)
cv2.waitKey(0)
