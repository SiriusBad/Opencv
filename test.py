import cv2
import numpy as np
dog=cv2.imread('hujiao.jpg')
dst = cv2.medianBlur(dog,9)
cv2.imshow('img', np.hstack((dog, dst)))
cv2.waitKey(0)
cv2.destroyAllWindows()

