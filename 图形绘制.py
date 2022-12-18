import cv2
import numpy as np

img = np.zeros((480, 640, 3), np.uint8)
"""line(img, pt1, pt2, color, thickness, lineType, shift) 画直线
         img: 在哪个图像上画线
         pt1, pt2: 开始点, 结束点. 指定线的开始与结束位置
         color: 颜色
         thickness: 线宽
         lineType: 线型.线型为-1, 4, 8, 16, 默认为8
         shift: 坐标缩放比例.
         
rectangle() 参数同上 画矩形

circle(img, center, radius, color[, thickness[, lineType[, shift]]]) 中括号内参数表示可选参数. 画圆

ellipse(img, 中心点, 长宽的一半, 角度, 从哪个角度开始, 从哪个角度结束,...)

polylines(img, pts, isClosed, color[, thickness[, lineType[, shift]]]) 画多边形

fillPoly 填充多边形

putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]]) 绘制文本
         text 要绘制的文本
         org 文本在图片中的左下角坐标
         fontFace 字体类型即字体
         fontScale 字体大小"""
# cv2.line(img, (10, 20), (300, 400), (0, 0, 255), 5, 4)
# cv2.line(img, (80, 100), (380, 480), (0, 0, 255), 5, 16)

# 画矩形
# cv2.rectangle(img, (10,10), (100, 100), (0, 0, 255), -1)         #提供任意一条对角线的两端点即可

# 画圆
# cv2.circle(img, (320, 240), 100, (0, 0, 255))
# cv2.circle(img, (320, 240), 5, (0, 0, 255), -1)
# 画椭圆
# cv2.ellipse(img, (320, 240), (100, 50), 15, 0, 360, (0, 0, 255), -1)

#画多边形
# pts = np.array([(300, 10), (150, 100), (450, 100)], np.int32)
# cv2.polylines(img, [pts], True, (0, 0, 255))

#填充多边形
# cv2.fillPoly(img, [pts], (255, 255, 0))
cv2.putText(img, "Hello OpenCV!", (10, 400), cv2.FONT_HERSHEY_TRIPLEX, 3, (255,0,0))
cv2.imshow('draw', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
