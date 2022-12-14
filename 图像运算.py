import cv2
import numpy as np
np.set_printoptions(threshold=np.inf)

cv2.namedWindow('sirius',cv2.WINDOW_NORMAL)
cv2.resizeWindow('sirius',840,525)

cat = cv2.imread('cat.jpg')
Dog = cv2.imread('dog.jpg')

dog = Dog[:1050,:1680]
"""加"""
new = cv2.add(cat,dog)
"""减"""
new1 = cv2.subtract(cat,dog)
"""乘"""
new2 = cv2.multiply(cat,dog)
"""除"""
new3 = cv2.divide(cat,dog)
# print(cat.shape)
# print(dog.shape)

# cv2.imshow('sirius',np.hstack((cat,dog)))
cv2.imshow('sirius',new3)
cv2.waitKey(0)
cv2.destroyAllWindows()