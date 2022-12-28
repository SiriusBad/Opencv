import cv2
import mediapipe as mp
import time


class HandDetector:
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        """
        static_image_mode=True适用于静态图片的手势识别，
  Flase适用于视频等动态识别，比较明显的区别是，若识别的手的数量超过了最大值，True时识别的手会在多个手之间不停闪烁，
  而False时，超出的手不会识别，系统会自动跟踪之前已经识别过的手。默认值为False。

        max_num_hands 用于指定识别手的最大数量。默认值为2。

        model_complexity 表示手部模型的复杂程度，手部模型越复杂，需要的响应时间就越长。默认值为1。

        min_detection_confidence 表示最小检测信度，取值为[0.0,1.0]这个值约小越容易识别出手，
  用时越短，但是识别的准确度就越差。越大识别的越精准，但是响应的时间也会增加。默认值为0.5。

        min_tracking_confience 表示最小的追踪可信度，越大手部追踪的越准确，相应的响应时间也就越长。默认值为0.5
"""
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands          # 手部识别api
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,
                                        self.detectionCon, self.trackCon)      # 获取手部识别类
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):         #标记
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        """process()是手势识别最核心的方法，通过调用这个方法，将窗口对象作为参数，mediapipe就会将手势识别的信息存入到res对象中"""
        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:        #数组字典
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):         #找坐标

        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = round(lm.x * w,2), round(lm.y * h,2)
                # print(id, cx, cy)
                lmList.append([id, cx, cy])
                # if draw:
                #     cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

        return lmList                #二十个点的坐标集


# def main():
#     pTime = 0
#     cTime = 0
#     cap = cv2.VideoCapture(1)
#     detector = handDetector()
#     while True:
#         success, img = cap.read()
#         img = detector.findHands(img)
#         lmList = detector.findPosition(img)
#         if len(lmList) != 0:
#             print(lmList[4])
#
#         cTime = time.time()
#         fps = 1 / (cTime - pTime)
#         pTime = cTime
#
#         cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
#                     (255, 0, 255), 3)
#
#         cv2.imshow("Image", img)
#         cv2.waitKey(1)


if __name__ == "__main__":
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(1)
    detector = HandDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        print(lmList)
        # if len(lmList) != 0:
        #     print(lmList[4])
        #
        cTime = time.time()
        fps = 1 / (cTime - pTime)             #  f = 1/T
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)

        cv2.imshow("Image", img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    cv2.destroyAllWindows()