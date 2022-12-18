import cv2

def callback(value):
    pass

cv2.namedWindow('sirius', cv2.WINDOW_NORMAL)
cv2.resizeWindow('sirius', 1800, 1080)

img = cv2.VideoCapture(1)

# 常见的颜色空间转换 2 = to
colorspaces = [cv2.COLOR_BGR2BGRA,cv2.COLOR_BGR2RGBA,
               cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2HSV,
               cv2.COLOR_BGR2YUV]
cv2.createTrackbar('colorspaces', 'sirius', 0, 4, callback)
while True:
    ret,frame = img.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)
    index = cv2.getTrackbarPos('colorspaces', 'sirius')
    frame = cv2.cvtColor(frame, colorspaces[index])
    cv2.imshow('sirius',frame)

    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

