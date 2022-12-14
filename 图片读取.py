import cv2
import matplotlib.pyplot as plt
import numpy as np

"""读取图片"""
img = cv2.imread('dog.jpg')

"""opencv读取的图片是BGR通道，不能用其他的读展示"""
# plt.imshow(img)
# plt.show()

def img_show(img,length,width):
    cv2.namedWindow('sirius', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('sirius',length,width)
    cv2.imshow('sirius', img)
    cv2.waitKey(0)
# img_show(img,960,600)

"""保存图片"""
def img_save(img,length,width):
    cv2.namedWindow('sirius', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('sirius',length,width)
    cv2.imshow('sirius', img)
    key = cv2.waitKey(0)
    if key == ord('s'):
        cv2.imwrite('1.jpg',img)
    else:
        cv2.destroyAllWindows()
# img_save(img,960,600)