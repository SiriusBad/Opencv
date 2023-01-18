import cv2
import time
import face_recognition
import os
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# from PIL import ImageGrab

path = 'ImagesAttendance'
images = []
encodeList = []
myList = os.listdir(path)
def read(cl):
    global images
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    return images

def findEncodings(images):
    global encodeList

    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

def find(images):
    List = []

    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        List.append(encode)
    return List

if __name__ == '__main__':
    t = time.time()
    with ThreadPoolExecutor() as pool:       #多线程
        pool.map(read ,myList)
    with ThreadPoolExecutor() as pool:
        encodeList = pool.map(find,images)
    print(encodeList)
    print('改进后时间:',time.time() - t)

    t = time.time()
    images = []
    myList = os.listdir(path)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
    print(find(images))
    print('时间:',time.time() - t)

