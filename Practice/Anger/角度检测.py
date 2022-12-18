import cv2
import math

path = 'anger.jpg'
img = cv2.imread(path)
pointsList = []

def mousePoints(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        size = len(pointsList)
        if size != 0 and size % 3 != 0:
            cv2.line(img, tuple(pointsList[0]), (x, y), (0, 0, 255), 2)
        cv2.circle(img, (x, y), 5, (0, 0, 255), cv2.FILLED)
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


    cv2.putText(img, str(angD), (pt1[0] - 40, pt1[1] - 20), cv2.FONT_HERSHEY_COMPLEX,1.5, (0, 0, 255), 2)


while True:

    if len(pointsList) % 3 == 0 and len(pointsList) != 0:
        getAngle(pointsList)

    cv2.imshow('Image', img)
    cv2.setMouseCallback('Image', mousePoints)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('c'):
        pointsList = []
        img = cv2.imread(path)
    if key & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()