import cv2
import numpy as np

np.set_printoptions(threshold=np.inf)

cv2.namedWindow('sirius',cv2.WINDOW_NORMAL)
cv2.resizeWindow('sirius',420*3,262)

cat = cv2.imread('cat.jpg')
Dog = cv2.imread('dog.jpg')
dog = Dog[:1050,:1680]

new = cv2.addWeighted(cat,0.3,dog,0.7,10)

cv2.imshow('sirius',np.hstack((cat,dog,new)))
# cv2.imshow('sirius',new3)
cv2.waitKey(0)
cv2.destroyAllWindows()