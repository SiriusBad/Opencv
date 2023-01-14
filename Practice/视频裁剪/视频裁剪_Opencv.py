import cv2

INPUT_FILE = '西游记1986_01.mkv'
OUTPUT_FILE1 = '第一集_上.mp4'
OUTPUT_FILE2 = '第一集_下.mp4'

reader = cv2.VideoCapture(INPUT_FILE)
width = int(reader.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(reader.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = reader.get(cv2.CAP_PROP_FPS)        #一秒多少帧
length = int(reader.get(cv2.CAP_PROP_FRAME_COUNT))      #一共多少帧
middle_frame = int(length / 2)
# print(width, height, fps, length)

writer1 = cv2.VideoWriter(OUTPUT_FILE1,
                         cv2.VideoWriter_fourcc(*'mp4v'),  # fourcc(*'mp4v') for mp4 format output
                         fps,  # fps
                         (width, height),True)
writer2 = cv2.VideoWriter(OUTPUT_FILE2,
                         cv2.VideoWriter_fourcc(*'mp4v'),
                         fps,
                         (width, height),True)
#
# print(reader.isOpened())
have_more_frame = True
c = -1
while have_more_frame:
    have_more_frame, frame = reader.read()
    c += 1
    if c <= middle_frame:
        cv2.waitKey(1)
        writer1.write(frame)
        print(str(c) + ' is ok')
    elif c > middle_frame and c <= length:
        writer1.write(frame)
        print(str(c) + ' is ok')
    else:
        break

writer1.release()
writer2.release()
reader.release()
cv2.destroyAllWindows()