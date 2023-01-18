import cv2
import numpy as np

dog = cv2.imread('dog.jpg')

"""方盒滤波"""
"""
boxFilter(src, ddepth, ksize[, dst[, anchor[, normalize[, borderType]]]]) 方盒滤波
    normalize = True时, a = 1 / (W * H) 滤波器的宽高
    normalize = False是. a = 1
一般情况我们都使用 normalize = True的情况. 这时 方盒滤波 等价于 均值滤波"""
dst = cv2.boxFilter(dog,-1,(5,5),normalize=True)
cv2.imshow('img', np.hstack((dog, dst)))
cv2.waitKey(0)
cv2.destroyAllWindows()


"""均值滤波"""
"""blur(src, ksize[, dst[, anchor[, borderType]]]) 均值滤波"""
dst = cv2.blur(dog,(5,5))
cv2.imshow('img', np.hstack((dog, dst)))
cv2.waitKey(0)
cv2.destroyAllWindows()


"""高斯滤波————可用于降噪"""
"""GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]])
      kernel 高斯核的大小.
      sigmaX, X轴的标准差
      sigmaY, Y轴的标准差, 默认为0, 这时sigmaY = sigmaX
如果没有指定sigma值, 会分别从ksize的宽度和高度中计算sigma.
"""
dst = cv2.GaussianBlur(dog,(5,5),sigmaX=10)
cv2.imshow('img', np.hstack((dog, dst)))
cv2.waitKey(0)
cv2.destroyAllWindows()


"""中值滤波————降低胡椒噪音"""
dst = cv2.medianBlur(dog,9)    #奇数
cv2.imshow('img', np.hstack((dog, dst)))
cv2.waitKey(0)
cv2.destroyAllWindows()


"""双边滤波————美颜"""
"""bilateralFilter(src, d, sigmaColor, sigmaSpace[, dst[, borderType]])
      sigmaColor是计算像素信息使用的sigma
      sigmaSpace是计算空间信息使用的sigma"""
dst = cv2.bilateralFilter(dog, 7, 20, 50)
cv2.imshow('img', np.hstack((dog, dst)))
cv2.waitKey(0)
cv2.destroyAllWindows()
