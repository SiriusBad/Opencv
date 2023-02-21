import cv2
import numpy as np
import face_recognition
import os
from multiprocessing import Pool

path = 'ImagesAttendance'
images = []
classNames = []
myList = os.listdir(path)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])


def findEncodings(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    encode = face_recognition.face_encodings(img)[0]
    return encode


if __name__ == '__main__':
    with Pool() as p:
        encodeListKnown = p.map(findEncodings, images)

    print('Encoding Complete')



