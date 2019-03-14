# NoBaseCode - Mohamed LAABID
# A Face Recognition script for authentication systems

import face_recognition
import cv2

video_capture = cv2.VideoCapture(0)
t = False


me_image = face_recognition.load_image_file("me.jpg")
me_face_encoding = face_recognition.face_encodings(me_image)[0]


known_face_encodings = [
    me_face_encoding
]
known_face_names = [
    "MOHAMED"
]

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

i = 0
while True:
    ret, frame = video_capture.read()

    small_frame = cv2.resize(frame, (0, 0), fx=0.20, fy=0.20)

    rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)

        # print(len(face_locations))
        if len(face_locations) == 1:
            # print(face_locations[0])
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            # print(face_encodings[0])
        
            match = face_recognition.compare_faces([me_face_encoding], face_encodings[0])
            name = "Unknown"
            
            if match[0] :
                i = i+1
                name = "Mohamed"

    if len(face_locations) == 1:

        process_this_frame = not process_this_frame

        (top, right, bottom, left) = face_locations[0]
        top *= 5
        right *= 5
        bottom *= 5
        left *= 5    
        cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)
        
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (255, 0, 0), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)                
        

    cv2.imshow('Video', frame)

    print(str(i))
    if i == 2:
        break
        video_capture.release()
        cv2.destroyAllWindows()
        t = True
        

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        video_capture.release()
        cv2.destroyAllWindows()

print("Permission Granted")
print("Welcome back Mohamed")

# video_capture.release()
# cv2.destroyAllWindows()