import cv2
import numpy as np

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

"""仿射变换是图像旋转, 缩放, 平移的总称.具体的做法是通过一个矩阵和和原图片坐标进行计算, 得到新的坐标, 完成变换. 所以关键就是这个矩阵.

warpAffine(src, M, dsize, flags, mode, value)

M:变换矩阵

dsize: 输出图片大小

flag: 与resize中的插值算法一致

mode: 边界外推法标志

value: 填充边界值
"""

"""getRotationMatrix2D(center, angle, scale)
    center 中心点 , 以图片的哪个点作为旋转时的中心点.
    angle 角度: 旋转的角度, 按照逆时针旋转.
    scale 缩放比例: 想把图片进行什么样的缩放."""

dog=cv2.imread('dog.jpg')
#获取原始图片的大小
h,w,ch=dog.shape
#获取变换矩阵 以点(300,480)为中心 旋转 15度 缩放比例为1
# print(h,w,ch)
M=cv2.getRotationMatrix2D((300,480),15,1)
#仿射变化
dog=cv2.warpAffine(dog,M,dsize=(w,h))
cv2.imshow('img',dog)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""getAffineTransform(src[], dst[]) 通过三点可以确定变换后的位置, 相当于解方程, 3个点对应三个方程, 能解出偏移的参数和旋转的角度.
    src原目标的三个点
    dst对应变换后的三个点"""
# 通过三个点来确定M
# 仿射变换之平移
dog=cv2.imread('dog.jpg')
h, w, ch = dog.shape

# 一般是横向和纵向的点, 所以一定会有2个点横坐标相同, 2个点纵坐标相同
src = np.float32([[200, 100], [300, 100], [200, 300]])
dst = np.float32([[100, 150], [360, 200], [280, 120]])
M = cv2.getAffineTransform(src, dst)
# 注意opencv中是先宽度, 再高度
new = cv2.warpAffine(dog, M, (w, h))

cv2.imshow('new', new)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""透视变换就是将一种坐标系变换成另一种坐标系. 简单来说可以把一张"斜"的图变"正",或者将一张 ‘正’ 图片 变 ‘斜’"""
dog=cv2.imread('dog.jpg')
print(dog.shape)
#获取变换矩阵
ori_point=np.float32([[10,10],[210,110],[0,350],[250,390]])
res_point=np.float32([[20,15],[230,110],[20,300],[300,350]])
M=cv2.getPerspectiveTransform(ori_point,res_point)

img2=cv2.warpPerspective(dog,M,dsize=(640,480))
cv2.imshow('img',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

