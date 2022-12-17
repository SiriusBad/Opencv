import cv2
import numpy as np

# cv2.namedWindow('sirius', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('sirius',960,600)


cap = cv2.VideoCapture(1)

while True:
    """读每一帧，返回标记和这一帧数据"""
    ret,frame = cap.read()

    """根据ret做判断"""
    if not ret:
        break

    """反转"""
    frame = cv2.flip(frame, 1)
    dst = cv2.bilateralFilter(frame, 9, 20, 50)
    cv2.imshow('sirius',np.hstack((frame, dst)))

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()