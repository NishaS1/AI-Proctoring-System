import cv2
import numpy as np

# Simplified: use color detection for phone/book (real project use YOLO)
def detect_objects(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Detect blue/red objects (phone)
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([130, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    if cv2.countNonZero(mask) > 5000:
        return ['cell phone']
    return []