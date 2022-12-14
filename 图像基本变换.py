import cv2

dog=cv2.imread('dog.jpg')

"""放大与缩小"""
#方式一：按照像素缩放  interpolation 可以指定算法 防止图片失真（一定会存在失真）
# dog=cv2.resize(dog,(800,800),interpolation=cv2.INTER_BITS)

"""方式二：按照 x,y轴比例进行缩放"""

"""resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])
src: 要缩放的图片
dsize: 缩放之后的图片大小, 元组和列表表示均可.
dst: 可选参数, 缩放之后的输出图片
fx, fy: x轴和y轴的缩放比, 即宽度和高度的缩放比.
interpolation: 插值算法, 主要有以下几种:
INTER_NEAREST, 邻近插值, 速度快, 效果差.
INTER_LINEAR, 双线性插值, 使用原图中的4个点进行插值. 默认.
INTER_CUBIC, 三次插值, 原图中的16个点.
INTER_AREA, 区域插值, 效果最好, 计算时间最长.
"""
new=cv2.resize(dog,dsize=None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
cv2.imshow('siri',dog)
cv2.imshow('sirius',new)
cv2.waitKey(0)
cv2.destroyAllWindows()


"""翻转"""
"""
flip(src, flipCode)
    flipCode =0 表示上下翻转
    flipCode >0 表示左右翻转
    flipCode <0 上下 + 左右"""
new1 = cv2.flip(dog, flipCode=0)
new2 = cv2.flip(dog, flipCode=1)
new3 = cv2.flip(dog, flipCode=-1)
cv2.imshow('0',dog)
cv2.imshow('1',new1)
cv2.imshow('2',new2)
cv2.imshow('3',new3)
cv2.waitKey(0)
cv2.destroyAllWindows()



"""旋转"""
"""
rotate(img, rotateCode)
    ROTATE_90_CLOCKWISE 90度顺时针
    ROTATE_180 180度
    ROTATE_90_COUNTERCLOCKWISE 90度逆时针"""
new_dog = cv2.rotate(dog, rotateCode=cv2.ROTATE_90_COUNTERCLOCKWISE)



"""仿射变换"""
