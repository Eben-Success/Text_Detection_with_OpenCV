import cv2
import pytesseract

pytesseract.pytesseract.t = "C:\Program Files\Tesseract-OCR"

img = cv2.imread("img")