import cv2
#旋转狗的图片
dog=cv2.imread('dog.jpg')
#获取原始图片的大小
h,w,ch=dog.shape
#获取变换矩阵 以点100,100为中心 旋转 15度 缩放比例为1
# print(h,w,ch)
M=cv2.getRotationMatrix2D((300,480),15,1)
#仿射变化
dog=cv2.warpAffine(dog,M,dsize=(w,h))
cv2.imshow('img',dog)
cv2.waitKey(0)
cv2.destroyAllWindows()


