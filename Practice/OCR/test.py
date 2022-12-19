import cv2
import math
import numpy as np

img = cv2.VideoCapture(1)
pointsList = []
ret, frame = img.read()
def mousePoints(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        size = len(pointsList)
        if size != 0 and size % 3 != 0:
            cv2.line(frame, tuple(pointsList[round((size-1)/3)*3]), (x, y), (0, 0, 255), 2)
        cv2.circle(frame, (x, y), 5, (0, 0, 255), cv2.FILLED)
        pointsList.append([x, y])


def gradient(pt1, pt2):
    x = pt2[0] - pt1[0]
    y = pt2[1] - pt1[1]
    if y>0 and x>0:
        return round(math.degrees(math.atan(y/x)),2)
    elif y>0 and x<0:
        return round(math.degrees(math.atan(y/x)),2)+180
    elif y<0 and x<0:
        return round(math.degrees(math.atan(y/x)),2)-180
    else:
        return round(math.degrees(math.atan(y / x)), 2)




def getAngle(pointsList):
    pt1, pt2, pt3 = pointsList[-3:]
    ang1 = gradient(pt1, pt2)
    ang2 = gradient(pt1, pt3)
    if round(abs(ang1-ang2),2)<180:
        angD = round(abs(ang1 - ang2), 2)
    else:
        angD = 360-round(abs(ang1 - ang2), 2)


    cv2.putText(frame, str(angD), (pt1[0] - 40, pt1[1] - 20), cv2.FONT_HERSHEY_COMPLEX,1.5, (0, 0, 255), 2)


while True:
    ret, frame = img.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    Frame = frame
    cv2.imshow('Image', frame)
    key2 = cv2.waitKey(1)
    if key2 & 0xFF == ord('b'):
        pointsList = []
        while True:
            if len(pointsList) % 3 == 0 and len(pointsList) != 0:
                getAngle(pointsList)
            cv2.imshow('I', frame)
            cv2.setMouseCallback('I', mousePoints)
            key1 = cv2.waitKey(1)
            if key1 & 0xFF == ord('q'):
                break
    if key2 & 0xFF == ord('q'):
        break

img.release()
cv2.destroyAllWindows()