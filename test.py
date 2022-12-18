import cv2
import numpy as np
from PIL import Image
import pytesseract
img = cv2.imread('1.jpg')
new=pytesseract.image_to_string(img,lang='chi_sim')
print(new)
