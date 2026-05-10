from flask import request, jsonify
from utils.face_detection import verify_face
from utils.eye_tracking import get_gaze_status
from utils.object_detection import detect_objects
from utils.audio_monitor import analyze_audio
from utils.suspicious_score import SuspiciousScore
import cv2
import numpy as np
import base64

score_tracker = SuspiciousScore()

def init_routes(app):

    @app.route('/verify-face', methods=['POST'])
    def verify_face_route():
        data = request.json['image']
        img_data = base64.b64decode(data.split(',')[1])
        np_arr = np.frombuffer(img_data, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        result = verify_face(frame)
        return jsonify({'verified': result})

    @app.route('/analyze-frame', methods=['POST'])
    def analyze_frame():
        data = request.json['image']
        img_data = base64.b64decode(data.split(',')[1])
        np_arr = np.frombuffer(img_data, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        # Face detection
        face_ok = verify_face(frame)

        # Eye tracking
        gaze = get_gaze_status(frame)

        # Object detection
        objects = detect_objects(frame)

        # Update score
        if not face_ok:
            score_tracker.add_event('multiple_faces')
        if gaze == 'away':
            score_tracker.add_event('looking_away')
        if 'cell phone' in objects or 'book' in objects:
            score_tracker.add_event('object_detected')

        return jsonify({
            'face_ok': face_ok,
            'gaze': gaze,
            'objects': objects,
            'score': score_tracker.get_score()
        })

    @app.route('/analyze-audio', methods=['POST'])
    def analyze_audio_route():
        audio_file = request.files['audio']
        result = analyze_audio(audio_file)
        if result:
            score_tracker.add_event('talking')
        return jsonify({'talking': result, 'score': score_tracker.get_score()})

    @app.route('/get-report', methods=['GET'])
    def get_report():
        return jsonify(score_tracker.get_report())