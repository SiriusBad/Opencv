import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(1)

while True:

    success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')        #读取信息并解码
        myColor = (0, 255, 0)

        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, myColor, 5)
        pts2 = barcode.rect
        cv2.putText(img, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX,0.9, myColor, 2)

    cv2.imshow('Result', img)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

# img.release()
cv2.destroyAllWindows()