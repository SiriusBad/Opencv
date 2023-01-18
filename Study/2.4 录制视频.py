import cv2

cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)
fourcc = cv2.VideoWriter_fourcc(*'XVID')

vw = cv2.VideoWriter('output.avi',fourcc,20,(640,480))

while True:
    ret, frame = cap.read()

    if not ret:
        print('can not recive frame, Exiting...')
        break

    vw.write(frame)
    cv2.imshow('frame', frame)

    key = cv2.waitKey(33)

    if  key & 0xFF == ord('q'):
        break

cap.release() #释放VideoWriter
cv2.destroyAllWindows()