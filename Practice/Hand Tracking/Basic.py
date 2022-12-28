import mediapipe as mp
import cv2

mpHands = mp.solutions.hands
hands = mpHands.Hands(False,2,0.5,0.5)
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(1)
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    lmList = []
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:  # 数组字典
            if True:
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    if results.multi_hand_landmarks:
        myHand = results.multi_hand_landmarks[0]
        for id, lm in enumerate(myHand.landmark):       #加索引
            # print(id, lm)
            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            # print(id, cx, cy)
            lmList.append([id, cx, cy])
            # if True:
            #     cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
    # lmList = detector.findPosition(img)
    # print(lmList)
    # if len(lmList) != 0:
    #     print(lmList[4])
    #
    # cTime = time.time()
    # fps = 1 / (cTime - pTime)  # f = 1/T
    # pTime = cTime
    #
    # cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
    #             (255, 0, 255), 3)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
