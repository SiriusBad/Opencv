"""https://blog.csdn.net/qq_43944517/article/details/126447584"""
"""filter2D(src, ddepth, kernel[, dst[, anchor[, delta[, borderType]]]])
    ddepth是卷积之后图片的位深, 即卷积之后图片的数据类型, 一般设为-1, 表示和原图类型一致.
    kernel是卷积核大小, 用元组或者ndarray表示, 要求数据类型必须是float型.
    anchor 锚点, 即卷积核的中心点, 是可选参数, 默认是(-1,-1)
    delta 可选参数, 表示卷积之后额外加的一个值, 相当于线性方程中的偏差, 默认是0.
    borderType 边界类型.一般不设.
"""
# OpenCV图像卷积操作
import cv2
import numpy as np

#导入图片
img = cv2.imread('dog.jpg')

# 相当于原始图片中的每个点都被平均了一下, 所以图像变模糊了.
kernel = np.ones((5, 5), np.float32) / 25
# ddepth = -1 表示图片的数据类型不变
dst = cv2.filter2D(img, -1, kernel)

# 很明显卷积之后的图片模糊了.
cv2.imshow('img', np.hstack((img, dst)))

cv2.waitKey(0)
cv2.destroyAllWindows()
