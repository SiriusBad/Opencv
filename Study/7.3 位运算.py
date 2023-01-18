import cv2
import numpy as np

np.set_printoptions(threshold=np.inf)

# cv2.namedWindow('sirius',cv2.WINDOW_NORMAL)
# cv2.resizeWindow('sirius',400,200)

Cat = cv2.imread('cat.jpg')
Dog = cv2.imread('dog.jpg')
# dog = Dog[:1050,:1680]
cat = Cat[:3,:4]
dog = Dog[:3,:4]

new1 = cv2.bitwise_and(cat,dog)
"""与运算
   参数：
    1）img1:图片对象1
    2）img2:图片对象2
    3）mask:掩膜"""

new2 = cv2.bitwise_or(cat,dog)
"""或运算
   参数：
   1）img1:图片对象1
   2）img2:图片对象2
   3）mask:掩膜"""

new3 = cv2.bitwise_xor(cat,dog)
"""异或运算
   参数：
  1）img1:图片对象1
  2）img2:图片对象2
  3）mask:掩膜"""

new4 = cv2.bitwise_not(cat)
"""非运算
   参数：
  1）img1:图片对象1
  2）mask:掩膜"""
print('cat:',cat)
print('dog:',dog)
print('new1:',new1)
# cv2.imshow('sirius',np.hstack((cat,dog)))
# cv2.imshow('sirius',new3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()