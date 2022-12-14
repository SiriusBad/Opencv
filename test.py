import cv2
import numpy as np
dog=cv2.imread('cat.jpg')
new=cv2.resize(dog,dsize=None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
cv2.imwrite('1.jpg',new)

