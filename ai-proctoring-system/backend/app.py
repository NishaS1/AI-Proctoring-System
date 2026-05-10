from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"status": "Proctoring System Running!"})

@app.route('/analyze-frame', methods=['POST'])
def analyze_frame():
    # Simplified version - always returns OK
    return jsonify({
        'face_ok': True,
        'gaze': 'center',
        'objects': [],
        'score': 0
    })

@app.route('/get-report', methods=['GET'])
def get_report():
    return jsonify({
        'score': 0,
        'events': [],
        'flagged': False
    })

if __name__ == '__main__':
    print("Server starting on http://localhost:5000")
    app.run(debug=True, port=5000)