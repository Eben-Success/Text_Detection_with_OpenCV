import cv2
import pytesseract

pytesseract.pytesseract.t = "C:\Program Files\Tesseract-OCR"

img = cv2.imread("img")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)