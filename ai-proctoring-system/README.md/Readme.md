# AI Proctoring System

## Setup
1. `cd backend && pip install -r requirements.txt`
2. `python database/init_db.py`
3. `python app.py` (starts backend on port 5000)
4. Open `frontend/exam.html` in browser (or serve with live-server)
5. Open `frontend/admin.html` for live monitoring

## Features
- Face detection (single face required)
- Eye tracking (gaze direction)
- Object detection (phone detection)
- Audio analysis (talking detection)
- Suspicious score (auto-flagging)

## Notes
- Ensure webcam and microphone permissions are granted.
- For production, replace simplified object detection with YOLO.