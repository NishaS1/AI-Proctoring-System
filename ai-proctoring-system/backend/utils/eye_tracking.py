import cv2
import numpy as np

def get_gaze_status(frame):
    """
    Simple gaze detection using face region analysis
    Returns: 'center', 'away', or 'no_face'
    """
    # Load face cascade
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    if len(faces) == 0:
        return 'no_face'
    
    # Get the largest face
    (x, y, w, h) = max(faces, key=lambda f: f[2] * f[3])
    
    # Calculate face center relative to frame
    frame_center_x = frame.shape[1] // 2
    face_center_x = x + w // 2
    
    # If face is significantly off-center, assume looking away
    threshold = frame.shape[1] * 0.15  # 15% of frame width
    
    if abs(face_center_x - frame_center_x) > threshold:
        return 'away'
    
    return 'center'