"""YOLO26 Webcam Object Detection"""

import cv2
from ultralytics import YOLO

# 1. Load the pretrained YOLOv8n nano model
model = YOLO("best.pt")

# 2. Open the default webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError("Could not open the webcam.")

print("Press 'q' in the video window to quit.")

try:
    while True:
        # 3. Read one image (frame) from the webcam
        success, frame = cap.read()
        if not success:
            print("Could not read a frame.")
            break

        # 4. Detect objects in the frame
        results = model(frame, conf=0.5)      #conf=0.5, verbose=False

        # 5. Draw bounding boxes, class names, and confidence scores
        annotated_frame = results[0].plot()

        # 6. Display the annotated frame
        cv2.imshow("YOLOv8 Webcam Detection", annotated_frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break
finally:
    # 7. Release the webcam and close the window
    cap.release()
    cv2.destroyAllWindows()