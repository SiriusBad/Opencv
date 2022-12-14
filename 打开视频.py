import cv2

cv2.namedWindow('sirius', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('sirius',540,400)

cap = cv2.VideoCapture('1.mp4')

while True:
    """读每一帧，返回标记和这一帧数据"""
    ret,frame = cap.read()

    """根据ret做判断"""
    if not ret:
        break

    cv2.imshow('sirius',frame)

    key = cv2.waitKey(33)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()