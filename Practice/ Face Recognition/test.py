import cv2
import face_recognition


imgElon = face_recognition.load_image_file('111.jpg')
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgElon)
encodeElon = face_recognition.face_encodings(imgElon)