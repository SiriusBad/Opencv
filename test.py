import cv2
import numpy as np
img = cv2.imread('dog.jpg')
dst = cv2.Laplacian(img, -1, ksize=3)
cv2.imshow('dx', np.hstack((img, dst)))
cv2.waitKey(0)
cv2.destroyAllWindows()

