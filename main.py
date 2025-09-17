import cv2
import numpy as np
import mediapipe as mp

def process_img(img, face_detection):
    H, W, _ = img.shape

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)

    if out.detections is not None :
        for detection in out.detections :
            location_data= detection.location_data
            bbox = location_data.relative_bounding_box

            x, y, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height
            x = int(x * W)
            y = int(y * H)
            w = int(w * W)
            h = int(h * H)

            if x < 0: x = 0
            if y < 0: y = 0
            if x + w > W: w = W - x
            if y + h > H: h = H - y

            if w > 0 and h > 0 :
                img[y: y + h, x: x + w, : ]= cv2.blur(img[y: y + h, x: x + w, : ], (35,35))
                cv2.rectangle(img, (x, y) , (x + w, y + h), (0, 255, 0), 2)
    return img


mp_face_detection = mp.solutions.face_detection 

with mp_face_detection.FaceDetection (model_selection=0, min_detection_confidence=0.5) as face_detection :
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Ignoring")
            continue
        
        frame = process_img(cv2.flip(frame, 1), face_detection)
        cv2.imshow('Face Blur', frame)

        if cv2.waitKey(5) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()