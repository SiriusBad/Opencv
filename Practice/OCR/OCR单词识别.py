import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import time

img = cv2.imread('ocr.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# #[   0          1           2           3           4          5         6       7       8        9        10       11 ]
# #['level', 'page_num', 'block_num', 'par_num', 'line_num', 'word_num', 'left', 'top', 'width', 'height',位置 'conf置信度', 'text识别出的文本']
boxes = pytesseract.image_to_data(img)
print(enumerate(boxes.splitlines()))          #enumerate对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值
for a,b in enumerate(boxes.splitlines()):
        print(b)
        if a!=0:                     #舍去第一行['level', 'page_num', 'block_num', 'par_num', 'line_num', 'word_num', 'left', 'top', 'width', 'height',位置 'conf置信度', 'text识别出的文本']
            b = b.split()
            if len(b)==12:
                x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
                cv2.putText(img,b[11],(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)
                cv2.rectangle(img, (x,y), (x+w, y+h), (50, 50, 255), 2)


##############################################
##### Detecting ONLY Digits  ######
##############################################
# hImg, wImg,_ = img.shape
# conf = r'--oem 3 --psm 6 outputbase digits'
# boxes = pytesseract.image_to_boxes(img,config=conf)
# for b in boxes.splitlines():
#     print(b)
#     b = b.split(' ')
#     print(b)
#     x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
#     cv2.rectangle(img, (x,hImg- y), (w,hImg- h), (50, 50, 255), 2)
#     cv2.putText(img,b[0],(x,hImg- y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)


##############################################
##### Webcam and Screen Capture Example ######
##############################################
# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# def captureScreen(bbox=(300,300,1500,1000)):
#     capScr = np.array(ImageGrab.grab(bbox))
#     capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
#     return capScr
# while True:
#     timer = cv2.getTickCount()
#     _,img = cap.read()
#     #img = captureScreen()
#     #DETECTING CHARACTERES
#     hImg, wImg,_ = img.shape
#     boxes = pytesseract.image_to_boxes(img)
#     for b in boxes.splitlines():
#         #print(b)
#         b = b.split(' ')
#         #print(b)
#         x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
#         cv2.rectangle(img, (x,hImg- y), (w,hImg- h), (50, 50, 255), 2)
#         cv2.putText(img,b[0],(x,hImg- y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)
#     fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
#     #cv2.putText(img, str(int(fps)), (75, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (20,230,20), 2);
#     cv2.imshow("Result",img)
#     cv2.waitKey(1)
#
#

cv2.imshow('img', img)
cv2.waitKey(0)