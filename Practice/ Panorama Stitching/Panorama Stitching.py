import cv2
import os

mainFolder = 'img'
myFolders = os.listdir(mainFolder)
# print(myFolders)
images =[]
for folder in myFolders:
    path = mainFolder +'/'+folder
    # print(path)

#     myList = os.listdir(path)
#     print(f'Total no of images detected {len(myList)}')
#     for imgN in myList:
    curImg = cv2.imread(path)
    curImg = cv2.resize(curImg,(0,0),None,0.2,0.2)
    images.append(curImg)
# print(len(images))
#
stitcher = cv2.Stitcher_create()
(status,result) = stitcher.stitch(images)
if (status == cv2.STITCHER_OK):
    print('Panorama Generated')
    cv2.imwrite('folder.jpg',result)
else:
    print('Panorama Generation Unsuccessful')
