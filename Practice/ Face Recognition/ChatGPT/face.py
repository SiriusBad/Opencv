import face_recognition
import cv2
import concurrent.futures
import os

KNOWN_FACES_DIR = 'known_faces'
TOLERANCE = 0.6
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = 'cnn'

def encode_known_faces():
    known_faces = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for file in os.listdir(KNOWN_FACES_DIR):
            image = face_recognition.load_image_file(os.path.join(KNOWN_FACES_DIR, file))
            future = executor.submit(face_recognition.face_encodings, image)
            face_encoding = future.result()
            if len(face_encoding) > 0:
                known_faces.append(face_encoding[0])
    return known_faces

known_faces = encode_known_faces()

video_capture = cv2.VideoCapture(1)

while True:
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_small_frame, model=MODEL)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_faces, face_encoding, tolerance=TOLERANCE)

        name = "Unknown"

        # If a match was found in known_faces, just use the first one.
        if True in matches:
            first_match_index = matches.index(True)
            name = os.listdir(KNOWN_FACES_DIR)[first_match_index].split(".")[0]

        # Draw a box around the face
        top, right, bottom, left = [i * 4 for i in face_locations[0]]
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), FRAME_THICKNESS)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), FONT_THICKNESS)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()

