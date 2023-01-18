import cv2
import numpy as np

img = cv2.imread('dog.jpg')
"""Sobel算子"""
# 注意 sobe 需要分别计算 X轴 和Y轴 梯度
#计算X轴方向梯度  效果 仅剩x轴格子 保留垂直方向边缘
dx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
#计算Y轴方向梯度  效果 仅剩Y轴格子 保留水平方向边缘
dy = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
dst = cv2.add(dx, dy)
cv2.imshow('dx', np.hstack((dx, dy, dst)))
cv2.waitKey(0)
cv2.destroyAllWindows()


"""Scharr算子"""
"""
Scharr算子只支持3 * 3 的kernel所以没有kernel参数了.
Scharr算子只能求x方向或y方向的边缘.
Sobel算子的ksize设为-1就是Scharr算子.
Scharr擅长寻找细小的边缘, 一般用的较少."""
dx = cv2.Scharr(img, cv2.CV_64F, 1, 0)
dy = cv2.Scharr(img, cv2.CV_64F, 0, 1)
dst = cv2.add(dx, dy)
cv2.imshow('dx', np.hstack((dx, dy, dst)))
cv2.waitKey(0)
cv2.destroyAllWindows()


"""拉普拉斯算子"""
dst = cv2.Laplacian(img, -1, ksize=3)
cv2.imshow('dx', np.hstack((img, dst)))
cv2.waitKey(0)
cv2.destroyAllWindows()
