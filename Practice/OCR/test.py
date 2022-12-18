import pytesseract
import cv2
import numpy as np

# cv2.namedWindow('sirius', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('sirius',960,600)


cap = cv2.VideoCapture(1)

while True:
    ret,frame = cap.read()
    if not ret:
        break
    # frame = cv2.flip(frame, 1)
    boxes = pytesseract.image_to_string(frame,lang='chi_sim')
    cv2.putText(frame, boxes, (100,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)
    cv2.imshow('sirius',frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()