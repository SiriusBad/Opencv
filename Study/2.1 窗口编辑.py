import cv2
import time
import matplotlib.pyplot as plt
import numpy as np

"""创建窗口"""
cv2.namedWindow('sirius',cv2.WINDOW_NORMAL)

"""更改大小"""
cv2.resizeWindow('sirius',800,600)

"""展示窗口"""
cv2.imshow('sirius',0)

"""等待按键"""
"""按键后关闭窗口，并返回ASCII"""
# print(cv2.waitKey(0))
"""5s后关闭"""
# cv2.waitKey(5000)
"""销毁所有窗口"""
# cv2.destroyAllWindows()
"""按下q关闭"""
key = cv2.waitKey(0)
if key==ord('q'):
    print('准备销毁窗口')
    cv2.destroyAllWindows()
else:
    time.sleep(100)