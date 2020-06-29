import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread("book_page-1309x1536.jpg")
img = cv2.resize(img, None, fx=0.5, fy=0.5)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 55, 11)

text = pytesseract.image_to_string(adaptive_threshold)
print(text)

# cv2.imshow('Img', img)
# cv2.imshow('Gray', gray)
cv2.imshow('adaptive threshold', adaptive_threshold)
cv2.waitKey(0)
