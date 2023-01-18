import cv2

def callback(value):
    pass

cv2.namedWindow('color', cv2.WINDOW_NORMAL)
cv2.resizeWindow('color', 960, 600)

img = cv2.imread('dog.jpg')

# 常见的颜色空间转换 2 = to
colorspaces = [cv2.COLOR_BGR2RGBA, cv2.COLOR_BGR2BGRA,
               cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2HSV,
               cv2.COLOR_BGR2YUV]
cv2.createTrackbar('colorspaces', 'color', 0, 4, callback)

while True:
    index = cv2.getTrackbarPos('colorspaces', 'color')

    #颜色空间转换API
    cvt_img = cv2.cvtColor(img, colorspaces[index])

    cv2.imshow('color', cvt_img)
    key = cv2.waitKey(10)
    if key & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
